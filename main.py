import bfs
originURL = input("Enter URL of origin: ")
size = int(input("Enter size of graph: "))
print(bfs.bfs(originURL, size))
