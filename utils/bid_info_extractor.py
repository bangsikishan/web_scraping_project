from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

def extract_bid_info(child_element, bid_no_xpath: str, title_xpath: str, due_date_xpath: str, index: int) -> tuple:
    try:
        bid_no_element = child_element.find_element(By.XPATH, bid_no_xpath.format(index=index))
        bid_no = bid_no_element.text[:20] or bid_no_element.get_attribute("textContent")[:20]
        
        title_element = child_element.find_element(By.XPATH, title_xpath.format(index=index))
        title = title_element.text[:40] or title_element.get_attribute("textContent")[:40]
        
        due_date_element = child_element.find_element(By.XPATH, due_date_xpath.format(index=index))
        due_date = due_date_element.text or due_date_element.get_attribute("textContent")

        return bid_no, title, due_date
    except NoSuchElementException:
        pass