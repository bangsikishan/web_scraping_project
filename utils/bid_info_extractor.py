from selenium.webdriver.common.by import By

def extract_bid_info(child_element, bid_no_xpath: str, title_xpath: str, due_date_xpath: str, index: int) -> tuple:
    bid_no = child_element.find_element(By.XPATH, bid_no_xpath.format(index=index)).text[:20]

    title = child_element.find_element(By.XPATH, title_xpath.format(index=index)).text[:40]

    due_date = child_element.find_element(By.XPATH, due_date_xpath.format(index=index)).text

    return bid_no, title, due_date
