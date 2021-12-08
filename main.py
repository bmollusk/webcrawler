import bfs
import networkx as nx
import matplotlib.pyplot as plt
from matplotlib import pylab
if __name__ == '__main__':
    originURL = input("Enter URL of origin: ")
    #https://en.wikipedia.org/wiki/MissingNo.
    size = int(input("Enter size of graph: "))
    G = bfs.bfb(originURL, size)
    print(G)

    # subax1=plt.subplot(121)
    # nx.draw(G, with_labels=True)
    # plt.show()
