import re
import requests
from urllib.parse import unquote

def download_file(url: str) -> tuple:
    if url is None:
        return
    
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.5666.197 Safari/537.36"
    }

    print(f"\n[+] Downloading from link {url}")
    response = requests.get(url, headers=headers)

    try:
        content_disposition = response.headers.get("Content-Disposition")
        filename = unquote(re.findall("filename=(.+)", content_disposition)[0])
    except AttributeError:
        filename = unquote(response.headers.get("x-full-url").split("/")[-1])
    except:
        filename = unquote(url.split("/")[-1])

    content_file_size_in_mb = int(response.headers.get('Content-Length')) / 1048576
    content_file_size_in_mb = str("{:.2f}".format(content_file_size_in_mb)) + " MB"

    with open(f"downloads\\{filename}", "wb") as write_file:
        write_file.write(response.content)

    return url, filename, content_file_size_in_mb