import httpx
import trio
from bs4 import BeautifulSoup
import socket
import random


async def get_all_links(url):
    user_agent_list = [
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:77.0) Gecko/20100101 Firefox/77.0',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:77.0) Gecko/20100101 Firefox/77.0',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36'
    ]
    user_agent = random.choice(user_agent_list)
    headers = {"User-Agent": user_agent}
    try:
        async with httpx.AsyncClient(limits=httpx.Limits(max_connections=7, max_keepalive_connections=6), timeout=60.0, headers=headers) as client:
            grab = await client.get(url)
            await trio.sleep(2)
            print(url, "URL")
            # if grab.status_code!=200:
            #     return []
            html = grab.text.encode('utf-8')
            soup = BeautifulSoup(html, 'html.parser')
            links = []
            for link in soup.find_all("a"):
                data = link.get('href')
                if isinstance(data, str):
                    if data.startswith("https://"):
                        links.append(data)
            return links
    except httpx.ConnectError as err:
        print("ERR", err)
        return []
    except httpx.RemoteProtocolError as err:
        print("EROR", err)
        return []
    except httpx.ReadError as err:
        print("ERRoR", err)
        return []
    except httpx.WriteError as err:
        print("ERROR", err)
        return []
    except UnicodeDecodeError as err:
        print("HUH", err)
        return []
    except OSError as err:
        print("YUH", err)
        return []
    except UnicodeError as err:
        print("YUH", err)
        return []