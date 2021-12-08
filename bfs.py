import getAllHyperlinks as gahl
import networkx as nx
import trio


def bfb(source, size):
    G = nx.DiGraph()
    q = [source]
    visited = set()
    # visited.add(source)

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
        p = q.copy()
        q = []
        async with trio.open_nursery() as nursery:
            for u in p:
                nursery.start_soon(explore, u, size)
            print(nursery.child_tasks)
    async with trio.open_nursery() as nursery:
        for v in q:
            nursery.start_soon(explorelite, v)
        print(nursery.child_tasks)
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
    neighbors = await gahl.get_all_links(v)
    for w in neighbors:
        if w in G:
            G.add_edge(v, w)
