import getAllHyperlinks as gahl
import networkx as nx
def bfs(source, size):
    G = nx.DiGraph()
    q = [source]
    visited = set()
    #visited.add(source)

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
    return G