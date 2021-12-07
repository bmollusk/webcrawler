import getAllHyperlinks
def bfs(source):
    output = []

    q = []
    visited = set()

    q.append(source)
    visited.add(source)

    while len(q)>0:
        u = q[0]

        output.append(u)

        q.pop()
        neighbors = getAllHyperlinks.get_all_links(u)
        for v in neighbors:
            if v in visited:
                q.append(v)
                visited.add(v)
    return output