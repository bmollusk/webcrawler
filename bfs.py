import getAllHyperlinks as gahl
import networkx as nx
import collections
import matplotlib.pyplot as plt
import trio


def dijkstra(G, originURL):
    computed = set()
    d={}
    p={}
    for n in G:
        d[n]=99999999
        p[n]="NO PREVIOUS SITE"
    d[originURL] = 0
    while len(computed)<G.number_of_nodes():
        smallest = -1
        for n in d:
            if n not in computed:
                if smallest == -1:
                    smallest = n
                if d[smallest] > d[n]:
                    smallest = n
        computed.add(smallest)
        for v in G[smallest]:
            if d[smallest] + 1 < d[v]:
                d[v] = d[smallest]+1
                p[v] = smallest
    return [d, p]




def dfs(G, originURL, URLtoFind):
    stack = [originURL]
    identified = set()
    identified.add(originURL)
    while len(stack)>0:
        u = stack.pop()
        for v in G[u]:
            if v not in identified:
                if v==URLtoFind:
                    return True
                identified.add(v)
                stack.append(v)
    return False

G = nx.DiGraph()
q = []
visited = set()


async def bfsasync(source, size):
    global G
    global q
    global visited
    q.append(source)
    # visited.add(source)

    G.add_node(source)

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
