def store_bid_details(bid_no: str, title: str, due_date: str, links: list, level: str, index: int) -> dict:
    bid_details = {
        index: {
            "bid_no": bid_no,
            "title": title,
            "due_date": due_date,
            "download_links" if int(level) == 0 else "page_links": links
        }
    }

    return bid_details
