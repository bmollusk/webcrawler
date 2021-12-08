import httpx
import trio
from bs4 import BeautifulSoup
import socket


async def get_all_links(url):
    async with httpx.AsyncClient(limits = httpx.Limits(max_connections=20, max_keepalive_connections=10), timeout=None) as client:
        grab = await client.get(url)
        print(url)
        await trio.sleep(1)
        html = grab.text
        soup = BeautifulSoup(html, 'html.parser')
        links = []
        for link in soup.find_all("a"):
            data = link.get('href')
            if isinstance(data, str):
                if data.startswith("https://"):
                    links.append(data)
        return links
