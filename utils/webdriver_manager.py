from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

def initialize_webdriver():
    service = Service(executable_path="chromedriver-win64\\chromedriver.exe")

    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--log-level=3")

    driver = webdriver.Chrome(service=service, options=chrome_options)
    
    return driver