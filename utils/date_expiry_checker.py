from datetime import datetime

def is_date_expired(date: str):
    if "not given" in date.lower():
        return False
    
    try:
        input_date = datetime.strptime(date, '%m/%d/%Y')
        
        current_date = datetime.now()

        if input_date < current_date:
            return True
        
        return False
    except Exception:
        raise RuntimeError("[-] Error in date_expiry_checker.py! Unable to check date!")