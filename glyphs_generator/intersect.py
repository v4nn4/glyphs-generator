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
