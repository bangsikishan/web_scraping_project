import time

from selenium.webdriver.common.by import By

from utils.webdriver_manager import initialize_webdriver
from utils.element_finder import find_child_elements
from utils.bid_info_extractor import extract_bid_info
from utils.link_filter import filter_unique_links
from utils.date_expiry_checker import is_date_expired
from utils.date_parser import parse_date
from utils.file_downloader import download_file
from utils.sha256_generator import generate_sha256
from utils.bid_details import store_bid_details

def get_bids(url: str, ecgains: str, level: str, bid_no_xpath: str, title_xpath: str, due_date_xpath: str, target_xpath: str, child_tagname: str, doc_container_xpath: str = None, doc_element_tagname: str = None):
    base_url = url
    bid_details = {}

    # Initialize web driver
    driver = initialize_webdriver()
    driver.get(base_url)
    time.sleep(2)

    # NOTE: THESE TWO LINES OF CODE ARE FOR IFRAMES ONLY
    # iframe = driver.find_element(By.XPATH, "//*[@id='main-content']/div/div[2]/iframe") 
    # driver.switch_to.frame(iframe)

    # Find child elements
    child_elements = find_child_elements(driver=driver, target_xpath=target_xpath, child_tagname=child_tagname)

    key = None
    for index, child_element in enumerate(child_elements, start=1):
        key = index
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

    # for keys, bid_detail in bid_details.items():
    #     driver.execute_script(f"window.open('{bid_detail['page_links'][0]}', '_blank');")
    #     driver.switch_to.window(driver.window_handles[1])
    #     time.sleep(2)

    #     doc_container = driver.find_element(By.XPATH, doc_container_xpath)
    #     doc_elements = doc_container.find_elements(By.TAG_NAME, doc_element_tagname)

    #     download_links = filter_unique_links(link_elements=doc_elements)

    #     bid_details[keys]["download_links"] = download_links

    #     driver.close()
    #     driver.switch_to.window(driver.window_handles[0])
    #     time.sleep(2)

    # import json
    # with open("temp\\output.json", "w") as f:
    #     json.dump(bid_details, f, indent=4)


    # for bid_detail in bid_details.items():
    #     download_links = bid_detail["download_links"]

    #     for link in download_links:
    #         file_url, file_name, file_size = download_file(url=link)
    #         hash = generate_sha256(ecgains=ecgains, bid_no=bid_detail["bid_no"], file_name=file_name)

    #         print(f"BID NO: {bid_detail['bid_no']}\nTITLE: {bid_detail['title']}\nDUE DATE: {bid_detail['due_date']}\nHASH: {hash}\nFILE URL: {file_url}\nFILE NAME: {file_name}\nFILE SIZE: {file_size}\n=======================================\n")
    
    driver.quit()