import getAllHyperlinks as gahl
import networkx as nx
def bfb(source, size):
    G = nx.DiGraph()
    q = [source]
    visited = set()

    while len(q)>0 and G.number_of_nodes()<size:
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