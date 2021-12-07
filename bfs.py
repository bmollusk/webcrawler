import getAllHyperlinks as gahl
import networkx as nx
def bfs(source, size):
    G = nx.DiGraph()
    q = [source]
    visited = set()
    visited.add(source)

    while len(q)>0 and G.number_of_nodes()<size:
        u = q[0]
        G.add_node(u)
        print(u, G.number_of_nodes(), "/", size, len(q))

        q.pop(0)
        neighbors = gahl.get_all_links(u)
        for v in neighbors:
            if len(q) + G.number_of_nodes() <= size:
                if v not in visited:
                    q.append(v)
                    visited.add(v)
                G.add_edge(u, v)
    return G