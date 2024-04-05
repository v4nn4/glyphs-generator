def orientation(x1, y1, x2, y2, x3, y3):
    """Return positive if (x1, y1), (x2, y2), (x3, y3) are clockwise, negative if counterclockwise, and 0 if collinear."""
    return (y2 - y1) * (x3 - x2) - (x2 - x1) * (y3 - y2)


def do_intersect(x1, y1, x2, y2, x3, y3, x4, y4):
    """Return True if line segments (x1, y1)-(x2, y2) and (x3, y3)-(x4, y4) intersect."""
    # Find the four orientations needed for the general and special cases
    o1 = orientation(x1, y1, x2, y2, x3, y3)
    o2 = orientation(x1, y1, x2, y2, x4, y4)
    o3 = orientation(x3, y3, x4, y4, x1, y1)
    o4 = orientation(x3, y3, x4, y4, x2, y2)

    # General case
    if o1 != o2 and o3 != o4:
        return True

    # Special Cases
    # (x1, y1), (x2, y2) and (x3, y3) are collinear and (x3, y3) lies on segment (x1, y1)-(x2, y2)
    if o1 == 0 and on_segment(x1, y1, x2, y2, x3, y3):
        return True
    # (x1, y1), (x2, y2) and (x4, y4) are collinear and (x4, y4) lies on segment (x1, y1)-(x2, y2)
    if o2 == 0 and on_segment(x1, y1, x2, y2, x4, y4):
        return True
    # (x3, y3), (x4, y4) and (x1, y1) are collinear and (x1, y1) lies on segment (x3, y3)-(x4, y4)
    if o3 == 0 and on_segment(x3, y3, x4, y4, x1, y1):
        return True
    # (x3, y3), (x4, y4) and (x2, y2) are collinear and (x2, y2) lies on segment (x3, y3)-(x4, y4)
    if o4 == 0 and on_segment(x3, y3, x4, y4, x2, y2):
        return True

    # If none of the cases
    return False


def on_segment(x1, y1, x2, y2, x3, y3):
    """Check whether (x3, y3) lies on line segment (x1, y1)-(x2, y2)."""
    if min(x1, x2) <= x3 <= max(x1, x2) and min(y1, y2) <= y3 <= max(y1, y2):
        return True
    return False
