import getAllHyperlinks
def bfs(source, size):
    output = []

    q = []
    visited = set()

    q.append(source)
    visited.add(source)

    while len(q)>0 and len(output)<=size:
        u = q[0]

        output.append(u)
        print(u, len(output), "/", size, len(q))

        q.pop(0)
        neighbors = getAllHyperlinks.get_all_links(u)
        if len(q) + len(output) <= size:
            for v in neighbors:
                if v not in visited:
                    q.append(v)
                    visited.add(v)
    return output