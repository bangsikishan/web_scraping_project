import os
import time

from dotenv import load_dotenv
from selenium.webdriver.common.by import By
from tqdm import tqdm

from utils.bid_details import store_bid_details
from utils.bid_info_extractor import extract_bid_info
from utils.child_element_validator import find_and_validate_elements
from utils.database_manager import create_database_session
from utils.date_expiry_checker import is_date_expired
from utils.date_parser import parse_date
from utils.element_finder import find_child_elements
from utils.file_downloader import download_file
from utils.final_steps import finalize
from utils.iframe_handler import find_element_in_iframe
from utils.level_one_handler import handle_level_one
from utils.link_filter import filter_unique_links
from utils.sha256_generator import generate_sha256
from utils.webdriver_manager import initialize_webdriver

def get_bids(url: str, ecgains: str, level: str, bid_no_xpath: str, title_xpath: str, due_date_xpath: str, target_xpath: str, child_tagname: str, doc_container_xpath: str = None, doc_element_tagname: str = None):
    # Get environment variables
    load_dotenv()
    db_host = os.getenv("DB_HOST")
    db_port = os.getenv("DB_PORT")
    db_user = os.getenv("DB_USER")
    db_password = os.getenv("DB_PASSWORD")
    db_name = os.getenv("DATABASE")
    
    base_url = url
    bid_details = {}

    # Start database connection
    database_url = f"mysql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"
    database_session = create_database_session(database_url=database_url)

    # Initialize web driver
    driver = initialize_webdriver()
    driver.get(base_url)
    time.sleep(2)

    # TODO: THIS IS CAUSING ERROR!!!
    # Switch the driver to iframe if bid is inside an iframe
    find_element_in_iframe(driver=driver, target_xpath=target_xpath)

    # Find child elements & verify those elements
    child_elements = find_child_elements(driver=driver, target_xpath=target_xpath, child_tagname=child_tagname)
    child_elements = find_and_validate_elements(elements=child_elements, title_xpath=title_xpath)

    if child_tagname == "a":
        for index, child_element in enumerate(child_elements, start=1):
            bid_no, title, due_date = extract_bid_info(child_element=child_element, bid_no_xpath=bid_no_xpath, title_xpath=title_xpath, due_date_xpath=due_date_xpath, index=index)
    
            due_date = parse_date(date=due_date)
            print(due_date)
            if is_date_expired(date=due_date):
                continue
            
            link = child_element.get_attribute("href")

            bid_details.update(store_bid_details(bid_no=bid_no, title=title, due_date=due_date, links=[link], level=level, index=index))
        
        finalize(ecgains=ecgains, bid_details=bid_details)
        return

    # Collect bid details
    print("[+] Collecting bid details...")
    for index, child_element in tqdm(enumerate(child_elements, start=1)):
        bid_no, title, due_date = extract_bid_info(child_element=child_element, bid_no_xpath=bid_no_xpath, title_xpath=title_xpath, due_date_xpath=due_date_xpath, index=index)
        
        due_date = parse_date(date=due_date)
        if is_date_expired(date=due_date):
            continue
        
        link_elements = child_element.find_elements(By.TAG_NAME, "a")
        filtered_links = filter_unique_links(link_elements=link_elements)

        if len(filtered_links) == 0:
            continue
    
        # Add bid details to dictionary
        bid_details.update(store_bid_details(bid_no=bid_no, title=title, due_date=due_date, links=filtered_links, level=level, index=index))

    # Further processing if website is of level one
    if int(level) == 1:
        handle_level_one(driver=driver, ecgains=ecgains, doc_container_xpath=doc_container_xpath, doc_element_tagname=doc_element_tagname, bid_details=bid_details)
    else:
        finalize(ecgains=ecgains, bid_details=bid_details)
    
    driver.quit()