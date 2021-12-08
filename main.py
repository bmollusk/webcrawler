import bfs
import networkx as nx
import matplotlib.pyplot as plt
import trio
from matplotlib import pylab
import time
if __name__ == '__main__':
    originURL = input("Enter URL of origin: ")
    #https://en.wikipedia.org/wiki/MissingNo.
    size = int(input("Enter size of graph: "))
    start_time = time.time()
    G = trio.run(bfs.bfsasync, originURL, size)
    print("--- %s seconds ---" % (time.time() - start_time))
    print(G)

    # subax1=plt.subplot(121)
    # nx.draw(G, with_labels=True)
    # plt.show()
