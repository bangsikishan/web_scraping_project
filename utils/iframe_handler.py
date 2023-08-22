from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

def find_element_in_iframe(driver, target_xpath: str):
    try:
        iframe_element = driver.find_element(By.TAG_NAME, "iframe")
        driver.switch_to.frame(iframe_element)
        driver.find_element(By.XPATH, target_xpath)
    except NoSuchElementException:
        driver.switch_to.default_content()