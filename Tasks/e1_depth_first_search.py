from typing import Hashable, List
import networkx as nx


def dfs_rec(g: nx.Graph, stack: list, node: str) -> List[Hashable]:
    stack.append(node)
    for _node in nx.neighbors(g, node):
        if _node not in stack:
            dfs_rec(g, stack, _node)
    return stack


def dfs(g: nx.Graph, start_node: Hashable) -> List[Hashable]:
    """
    Do an depth-first search and returns list of nodes in the visited order

    :param g: input graph
    :param start_node: starting node of search
    :return: list of nodes in the visited order
    """
    stack = dfs_rec(g, [], start_node)
    return stack
