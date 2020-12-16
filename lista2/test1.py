import networkx as nx
import matplotlib.pyplot as plt
from numpy import linspace
from lista2 import test1, assign_capacity, assign_flow, T

G = nx.disjoint_union(nx.cycle_graph(9), nx.cycle_graph(11))
for i in range(9):
    G.add_edge(i, i + 10)


N = [
    [0, 3, 2, 3, 6, 9, 8, 6, 9, 5, 4, 8, 6, 9, 2, 9, 7, 8, 9, 6],
    [1, 0, 2, 1, 2, 3, 4, 1, 4, 1, 1, 4, 8, 7, 1, 4, 3, 6, 5, 4],
    [4, 8, 0, 7, 3, 1, 4, 4, 6, 2, 5, 7, 1, 2, 8, 6, 1, 5, 8, 4],
    [2, 3, 6, 0, 1, 2, 6, 2, 1, 6, 9, 1, 5, 1, 2, 1, 8, 2, 3, 2],
    [4, 8, 5, 2, 0, 2, 4, 3, 4, 8, 6, 1, 1, 2, 3, 4, 2, 7, 8, 7],
    [1, 7, 5, 9, 2, 0, 2, 2, 5, 7, 3, 3, 2, 4, 1, 3, 2, 9, 9, 2],
    [7, 5, 3, 3, 3, 6, 0, 6, 1, 8, 4, 9, 4, 9, 1, 6, 1, 1, 9, 5],
    [3, 5, 9, 7, 5, 5, 5, 0, 5, 2, 6, 4, 7, 2, 4, 8, 7, 9, 6, 4],
    [4, 5, 5, 2, 6, 5, 7, 9, 0, 6, 2, 2, 7, 3, 5, 1, 4, 5, 8, 5],
    [4, 3, 6, 3, 7, 6, 5, 8, 8, 0, 7, 3, 7, 6, 3, 9, 5, 9, 1, 4],
    [6, 5, 8, 1, 6, 8, 8, 3, 6, 2, 0, 1, 6, 5, 2, 7, 6, 7, 7, 1],
    [2, 1, 5, 6, 7, 4, 2, 6, 8, 8, 3, 0, 4, 7, 7, 2, 1, 1, 9, 6],
    [6, 2, 2, 3, 5, 5, 2, 5, 6, 5, 1, 9, 0, 9, 9, 4, 9, 6, 7, 6],
    [8, 4, 8, 6, 5, 5, 5, 3, 4, 3, 3, 5, 7, 0, 4, 6, 7, 9, 7, 1],
    [4, 2, 1, 3, 7, 9, 1, 9, 6, 8, 1, 3, 7, 7, 0, 4, 7, 6, 5, 7],
    [7, 6, 4, 7, 2, 9, 7, 2, 7, 3, 8, 2, 2, 1, 9, 0, 8, 8, 1, 7],
    [5, 9, 5, 9, 2, 1, 6, 1, 6, 6, 4, 2, 9, 8, 6, 2, 0, 7, 6, 9],
    [7, 3, 4, 8, 5, 5, 7, 2, 9, 6, 3, 2, 4, 3, 7, 9, 1, 0, 1, 9],
    [1, 4, 9, 4, 6, 6, 4, 2, 2, 4, 9, 9, 2, 5, 1, 8, 3, 1, 0, 3],
    [2, 6, 4, 4, 9, 4, 9, 4, 7, 6, 2, 1, 2, 2, 8, 3, 3, 5, 2, 0],
]

assign_flow(G, N)
assign_capacity(G, N)

suma = sum(sum(r) for r in N)
min_Tmax = [T(G, suma, m) for m in range(1, 11)]

for m in range(10, 0, -2):
    startT = min_Tmax[m - 1]
    for p in linspace(0.9, 0.99, num=5):
        plt.figure()
        plt.imshow(
            [
                test1(G, N, Tmax, p, m, step=100)
                for Tmax in linspace(startT, 10 * startT, num=5)
            ],
            extent=[0, 1000, startT, 10 * startT],
            aspect="auto",
            origin="lower",
        )
        plt.colorbar()
        plt.ylabel("T_max")
        plt.xlabel("Liczba dodanych pakietów przy p={}, m={}".format(p, m))
        plt.savefig("TEST1_{}_{}.png".format(m, p))
        plt.close()
