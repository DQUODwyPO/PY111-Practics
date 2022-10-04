from typing import Hashable, Mapping, Union
import networkx as nx
import math
import heapq as hq


def dijkstra(G, s):
    visited = dict()
    weights = dict()
    path = dict()
    for d in G.nodes:
        weights[d] = math.inf
        visited[d] = False
        path[d] = None
    queue = []
    weights[s] = 0
    hq.heappush(queue, (0, s))
    while len(queue) > 0:
        g, u = hq.heappop(queue)
        visited[u] = True
        #print(G[u], u)
        for v, w in G[u].items():
            if not visited[v]:
                f = g + w['weight']
                if f < weights[v]:
                    weights[v] = f
                    path[v] = u
                    hq.heappush(queue, (f, v))
    return path, weights


def dijkstra_algo(g: nx.DiGraph, starting_node: Hashable) -> Mapping[Hashable, Union[int, float]]:
    """
    Count shortest paths from starting node to all nodes of graph g
    :param g: Graph from NetworkX
    :param starting_node: starting node from g
    :return: dict like {'node1': 0, 'node2': 10, '3': 33, ...} with path costs, where nodes are nodes from g
    """
    return dijkstra(g, starting_node)[1]
