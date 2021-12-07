import requests
from bs4 import BeautifulSoup

def get_all_links(url):
    headers = requests.utils.default_headers()

    headers.update(
        {
            'User-Agent': 'My User Agent 1.0',
        }
    )
    grab = requests.get(url, headers=headers)
    soup = BeautifulSoup(grab.text, 'html.parser')
    links = []
    for link in soup.find_all("a"):
        data = link.get('href')
        if isinstance(data, str):
            if "https" in data:
                links.append(data)
    return links