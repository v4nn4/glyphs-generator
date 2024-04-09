from typing import List


def on_segment(x1, y1, x2, y2, x3, y3):
    """Check if point (x3, y3) lies on the line segment (x1, y1) to (x2, y2)"""
    return x3 <= max(x1, x2) and x3 >= min(x1, x2) and y3 <= max(y1, y2) and y3 >= min(y1, y2)


def direction(x1, y1, x2, y2, x3, y3):
    """Find the direction of point (x3, y3) from the line segment (x1, y1) to (x2, y2)"""
    val = (y2 - y1) * (x3 - x2) - (x2 - x1) * (y3 - y2)
    if val == 0:
        return 0  # colinear
    return 1 if val > 0 else -1  # clockwise or counterclockwise


def do_intersect(x1, y1, x2, y2, x3, y3, x4, y4):
    """Check if segments (x1, y1, x2, y2) and (x3, y3, x4, y4) intersect"""
    d1 = direction(x3, y3, x4, y4, x1, y1)
    d2 = direction(x3, y3, x4, y4, x2, y2)
    d3 = direction(x1, y1, x2, y2, x3, y3)
    d4 = direction(x1, y1, x2, y2, x4, y4)

    # General case
    if d1 != d2 and d3 != d4:
        return True

    # Special Cases
    if d1 == 0 and on_segment(x3, y3, x4, y4, x1, y1):
        return True
    if d2 == 0 and on_segment(x3, y3, x4, y4, x2, y2):
        return True
    if d3 == 0 and on_segment(x1, y1, x2, y2, x3, y3):
        return True
    if d4 == 0 and on_segment(x1, y1, x2, y2, x4, y4):
        return True

    return False  # No intersection


def dfs(node: int, visited: set, subgraph: List[List[int]], stroke_indices: dict):
    """
    Depth-First Search to mark all nodes reachable from the current node.

    :param node: Current node being visited.
    :param visited: Set of already visited nodes.
    :param adjacency_matrix: Matrix indicating edges between nodes.
    """
    visited.add(node)
    for neighbor in range(len(subgraph)):
        if subgraph[node][neighbor] and neighbor not in visited:
            dfs(neighbor, visited, subgraph, stroke_indices)


def are_strokes_linked(strokes: List[int], intersection_matrix: List[List[int]]) -> bool:
    """
    Determines if the specified strokes are linked based on a subgraph of the intersection matrix.

    :param strokes: List of stroke indices to check.
    :param intersection_matrix: Full intersection matrix.
    :return: True if all specified strokes are linked, False otherwise.
    """
    if not strokes:
        return False

    # Create a subgraph that includes only the strokes of interest.
    stroke_indices = {stroke: idx for idx, stroke in enumerate(strokes)}
    subgraph = [[0 for _ in strokes] for _ in strokes]
    for i, stroke1 in enumerate(strokes):
        for j, stroke2 in enumerate(strokes):
            subgraph[i][j] = intersection_matrix[stroke1][stroke2]

    visited = set()
    # Start DFS from the first stroke in the subgraph
    dfs(0, visited, subgraph, stroke_indices)

    # Check if all strokes in the subgraph are reachable (visited)
    return len(visited) == len(strokes)
