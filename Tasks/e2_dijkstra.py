from typing import Hashable, Mapping, Union
import networkx as nx


def dijstra_rec(g: nx.DiGraph, size, end, start) -> Union[int, float]:
    pass


def dijkstra(g: nx.DiGraph, end, start) -> Union[int, float]:
    for node in nx.neighbors(g, start):
        if node == end:
            return g[start][node]
        else:
            return dijstra_rec(g, g[start][node], end, node)


def dijkstra_algo(g: nx.DiGraph, starting_node: Hashable) -> Mapping[Hashable, Union[int, float]]:
    """
    Count shortest paths from starting node to all nodes of graph g
    :param g: Graph from NetworkX
    :param starting_node: starting node from g
    :return: dict like {'node1': 0, 'node2': 10, '3': 33, ...} with path costs, where nodes are nodes from g
    """
    paths = dict()
    nodes = nx.nodes(g)
    for node in nodes:
        paths[node] = dijkstra(g, node, starting_node)
    return paths
