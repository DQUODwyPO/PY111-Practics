from typing import Hashable, List
import networkx as nx


def bfs(g: nx.Graph, start_node: Hashable) -> List[Hashable]:
    """
    Do an breadth-first search and returns list of nodes in the visited order

    :param g: input graph
    :param start_node: starting node for search
    :return: list of nodes in the visited order
    """
    stack = []
    visited = []
    stack.append(start_node)
    while stack:
        node = stack.pop()
        visited.append(node)
        for _node in nx.neighbors(g, node):
            if _node not in visited and _node not in stack:
                stack.insert(0, _node)
    return visited



