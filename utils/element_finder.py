from selenium.webdriver.common.by import By

def find_child_elements(driver, target_xpath: str, child_tagname: str) -> list:
    target_element = driver.find_element(By.XPATH, target_xpath)

    if child_tagname == "./*":
        return target_element.find_elements(By.XPATH, "./*")
    
    child_elements = target_element.find_elements(By.TAG_NAME, child_tagname)
    return child_elements