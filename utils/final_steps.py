from utils.file_downloader import download_file
from utils.sha256_generator import generate_sha256

def finalize(ecgains: str, bid_details: dict):
    for bid_detail in bid_details.items():
        download_links = bid_detail["download_links"]

        for link in download_links:
            file_url, file_name, file_size = download_file(url=link)
            hash = generate_sha256(ecgains=ecgains, bid_no=bid_detail["bid_no"], file_name=file_name)

            
            print(f"BID NO: {bid_detail['bid_no']}\nTITLE: {bid_detail['title']}\nDUE DATE: {bid_detail['due_date']}\nHASH: {hash}\nFILE URL: {file_url}\nFILE NAME: {file_name}\nFILE SIZE: {file_size}\n=======================================\n")