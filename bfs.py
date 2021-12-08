import getAllHyperlinks as gahl
import networkx as nx
import asyncio as ao


def bfb(source, size):
    G = nx.DiGraph()
    q = [source]
    visited = set()
    #visited.add(source)

    while len(q) > 0 and G.number_of_nodes() < size:
        u = q[0]
        print(u, G.number_of_nodes(), "/", size, len(q))

        q.pop(0)
        if u not in visited:
            neighbors = gahl.get_all_links(u)
            visited.add(u)
            for v in neighbors:
                if G.number_of_nodes() == size:
                    break
                q.append(v)
                G.add_edge(u, v)

    for v in q:
        print(v, G.number_of_nodes(), G.number_of_edges(), )
        neighbors = gahl.get_all_links(v)
        for w in neighbors:
            if w in G:
                G.add_edge(v, w)

    return G


G = nx.DiGraph()
q = []
visited = set()



async def bfsasync(source, size):
    global G
    global q
    global visited
    q.append(source)
    # visited.add(source)

    while len(q) > 0 and G.number_of_nodes() < size:
        tasks = []
        p = q.copy()
        q = []
        for u in p:
            tasks.append(ao.create_task(explore(u, size)))
        print(ao.all_tasks())
        await ao.gather(*tasks)
    tasks = []
    for v in q:
        tasks.append(ao.create_task(explorelite(v)))
    print(ao.all_tasks())
    await ao.gather(*tasks)

    return G


async def explore(u, size):
    global G
    global q
    global visited
    print(u, G.number_of_nodes(), "/", size, len(q))

    if G.number_of_nodes() >= size:
        return

    if u not in visited:
        neighbors = await gahl.get_all_links(u)
        visited.add(u)
        for v in neighbors:
            if G.number_of_nodes() == size:
                break
            q.append(v)
            G.add_edge(u, v)

async def explorelite(v):
    print(v, G.number_of_nodes(), G.number_of_edges(), )
    neighbors = gahl.get_all_links(v)
    for w in neighbors:
        if w in G:
            G.add_edge(v, w)

async def bfsrecurse(u, G, visited, size):
    G.add_node(u)
    print(u, G.number_of_nodes(), "/", size)

    neighbors = gahl.get_all_links(u)
    for v in neighbors:
        if G.number_of_nodes() == size:
            break
        if v not in visited:
            visited.add(v)
            await ao.create_task(bfsrecurse(v, G, visited, size))
        G.add_edge(u, v)


async def bfsmp(source, _size):
    G = nx.DiGraph()
    visited = set()
    size = 0

    visited.add(source)
    size = _size

    await ao.create_task(bfsrecurse(source, G, visited, size))

    return G
