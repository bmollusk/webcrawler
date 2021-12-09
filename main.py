import bfs
import networkx as nx
import plotly.graph_objects as go
import matplotlib.pyplot as plt
import trio
from matplotlib import pylab
import time

async def main():
    originURL = input("Enter URL of origin: ").strip()
    # https://en.wikipedia.org/wiki/MissingNo.
    size = int(input("Enter size of graph: "))
    start_time = time.time()
    G = await bfs.bfsasync(originURL, size)
    print("--- %s seconds ---" % (time.time() - start_time))
    print(G.number_of_nodes(), G.number_of_edges())

    # nx.draw_random(G)
    # plt.show()

    # net = Network(notebook=True)
    # net.from_nx(G)
    # net.show("example.html")


if __name__ == '__main__':
    trio.run(main)
