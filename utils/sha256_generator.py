import hashlib

def generate_sha256(ecgains: str, bid_no: str, file_name: str):
    if None in (ecgains, bid_no, file_name):
        raise ValueError("[-] Error in sha256_generator.py! Value cannot be None!")

    data_to_hash = f"{ecgains}{bid_no}{file_name}"

    data_bytes = data_to_hash.encode("utf-8")

    sha256_hash = hashlib.sha256(data_bytes).hexdigest()

    return sha256_hash