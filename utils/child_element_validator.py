from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

def find_and_validate_elements(elements, title_xpath: str):
    child_elements = []

    for index, element in enumerate(elements, start=1):
        try:
            element.find_element(By.XPATH, title_xpath.format(index=index))
            child_elements.append(element)
        except NoSuchElementException:
            continue

    return child_elements