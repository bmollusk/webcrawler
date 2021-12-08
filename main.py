import bfs
import networkx as nx
import matplotlib.pyplot as plt
originURL = input("Enter URL of origin: ")
#https://en.wikipedia.org/wiki/MissingNo.
size = int(input("Enter size of graph: "))
G = bfs.bfs(originURL, size)
print(G)
subax1=plt.subplot(121)
nx.draw(G, with_labels=True)
plt.show()
