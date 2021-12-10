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
    run=True
    while run:
        print("\n\n\n")
        print("1. Find if there is a path between two websites")
        print("2. Find the shortest path between all websites in graph")
        print("3. Exit")
        option = int(input("Select option: "))
        if option==1:
            originURL = input("Enter URL to search from: ").strip()
            if originURL not in G:
                print("URL is not within the graph")
            else:
                URLtoFind = input("Enter URL to locate: ").strip()
                if bfs.dfs(G, originURL, URLtoFind):
                    print("There is a path between the websites")
                else:
                    print("There is no path between the websites")
        if option==2:
            originURL = input("Enter URL to search from: ").strip()
            if originURL not in G:
                print("URL is not within the graph")
            else:
                dl=bfs.dijkstra(G, originURL)
                for n in dl[0]:
                    print("Distance from given URL: ", dl[0][n], "  :  ", n, "    previous: ", dl[1][n],"\n")
        if option==3:
            run=False

    # nx.draw_random(G)
    # plt.show()

    # net = Network(notebook=True)
    # net.from_nx(G)
    # net.show("example.html")


if __name__ == '__main__':
    trio.run(main)
