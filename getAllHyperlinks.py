import aiohttp
import asyncio
from bs4 import BeautifulSoup
import socket


async def get_all_links(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as grab:
            print(url)
            html = await grab.text()
            soup = BeautifulSoup(html, 'lxml')
            links = []
            for link in soup.find_all("a"):
                data = link.get('href')
                if isinstance(data, str):
                    if data.startswith("https://"):
                        links.append(data)
            return links
