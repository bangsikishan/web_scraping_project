import glob
import configparser

from SMI.smi import get_bids

def read_ini_config():
    config_file = glob.glob("config\\*.ini")

    if len(config_file) == 0 or len(config_file) > 1:
        print("[-] Only one config file should exist inside the config folder!")
        return
    
    config = configparser.ConfigParser()
    config.read(config_file)

    name = config.get('TEST', 'NAME')
    ecgains = config.get('TEST', 'ECGAINS')
    base_url = config.get('TEST', 'BASE_URL')
    level = config.get('TEST', 'LEVEL')
    title_xpath = config.get('TEST', 'TITLE_XPATH')
    bid_no_xpath = config.get('TEST', 'BID_NO_XPATH')
    due_date_xpath = config.get('TEST', 'DUE_DATE_XPATH')
    doc_container_xpath = config.get('TEST', 'DOC_CONTAINER_XPATH')
    doc_element_tagname = config.get('TEST', 'DOC_ELEMENT_TAGNAME')
    target_xpath = config.get('TEST', 'TARGET_XPATH')
    child_tagname = config.get('TEST', 'CHILD_TAGNAME')

    return name, ecgains, base_url, level, title_xpath, bid_no_xpath, due_date_xpath, doc_container_xpath, doc_element_tagname, target_xpath, child_tagname


(
    name, 
    ecgains, 
    base_url, 
    level, 
    title_xpath, 
    bid_no_xpath, 
    due_date_xpath, 
    doc_container_xpath, 
    doc_element_tagname, 
    target_xpath, 
    child_tagname
) = read_ini_config()


get_bids(
    url=base_url, 
    ecgains=ecgains, 
    level=level, 
    bid_no_xpath=bid_no_xpath, 
    title_xpath=title_xpath, 
    due_date_xpath=due_date_xpath, 
    doc_container_xpath=doc_container_xpath, 
    doc_element_tagname=doc_element_tagname, 
    target_xpath=target_xpath, 
    child_tagname=child_tagname
)