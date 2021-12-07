import getAllHyperlinks
def bfs(source):
    output = []

    q = []
    visited = set()

    q.append(source)
    visited.add(source)

    while len(q)>0 and len(output)<1000:
        u = q[0]

        output.append(u)
        print(u, len(output), "/1000")

        q.pop(0)
        neighbors = getAllHyperlinks.get_all_links(u)
        for v in neighbors:
            if v not in visited:
                q.append(v)
                visited.add(v)
    return output