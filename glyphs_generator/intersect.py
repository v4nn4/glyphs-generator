def do_intersect(x1: float, y1: float, x2: float, y2: float, x3: float, y3: float, x4: float, y4: float):
    """
    Returns the point of intersection of the lines passing through the points (x1, y1), (x2, y2) and (x3, y3), (x4, y4).
    Returns None if the lines don't intersect or are coincident/parallel.
    """
    # Calculate denominators
    den = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)

    # Parallel or coincident lines
    if den == 0:
        return False

    # Calculate numerators
    t_num = (x1 - x3) * (y3 - y4) - (y1 - y3) * (x3 - x4)
    u_num = -((x1 - x2) * (y1 - y3) - (y1 - y2) * (x1 - x3))

    # Calculate parameters t and u
    t = t_num / den
    u = u_num / den

    # Check if t and u lie between 0 and 1 for line segment intersection
    if 0 <= t <= 1 and 0 <= u <= 1:
        return True
    else:
        return False
