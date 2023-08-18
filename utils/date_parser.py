from dateparser.search import search_dates

def parse_date(date: str):
    try:
        result = search_dates(date)
        date_obj = result[0][1]
        date_str = date_obj.strftime('%m/%d/%Y')
        return date_str
    except Exception:
        # print(f"[-] Error in date_parser.py! Unable to parse date {date}!")
        return "Not Given"
        