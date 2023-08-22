import time

from selenium.webdriver.common.by import By
from tqdm import tqdm

from utils.link_filter import filter_unique_links

def handle_level_one(driver, doc_container_xpath: str, doc_element_tagname: str, bid_details: dict):
    print("\n[+] Processing level 1...")
    for keys, bid_detail in tqdm(bid_details.items()):
        driver.execute_script(f"window.open('{bid_detail['page_links'][0]}', '_blank');")
        driver.switch_to.window(driver.window_handles[1])
        time.sleep(2)

        doc_container = driver.find_element(By.XPATH, doc_container_xpath)
        doc_elements = doc_container.find_elements(By.TAG_NAME, doc_element_tagname)

        download_links = filter_unique_links(link_elements=doc_elements)

        bid_details[keys]["download_links"] = download_links

        driver.close()
        driver.switch_to.window(driver.window_handles[0])
        time.sleep(2)

    import json
    with open("temp\\output.json", "w") as f:
        json.dump(bid_details, f, indent=4)