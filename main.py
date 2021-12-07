import bfs
import networkx as nx
originURL = input("Enter URL of origin: ")
size = int(input("Enter size of graph: "))
print(bfs.bfs(originURL, size))
