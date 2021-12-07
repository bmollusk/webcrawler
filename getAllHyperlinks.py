import requests
from bs4 import BeautifulSoup

def get_all_links(url):
    grab = requests.get(url)
    soup = BeautifulSoup(grab.text, 'html.parser')
    links = []
    for link in soup.find_all("a"):
        data = link.get('href')
        if isinstance(data, str):
            if "https" in data:
                links.append(data)
    return links

# url = 'https://en.wikipedia.org/wiki/MissingNo.'
# grab = requests.get(url)
# soup = BeautifulSoup(grab.text, 'html.parser')
#
# f = open("test1.txt", "w")
# for link in soup.find_all("a"):
#     data = link.get('href')
#     if isinstance(data, str):
#         if "https" in data:
#             f.write(data)
#             f.write("\n")
#
# f.close()