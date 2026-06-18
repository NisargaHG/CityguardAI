def calculate_uds(priority, road_closure, event_type):

    score = 0

    # Priority Weight
    if str(priority).lower() == "high":
        score += 50
    else:
        score += 20

    # Road Closure Weight
    if str(road_closure).lower() == "true":
        score += 30

    # Event Type Weight
    if str(event_type).lower() == "unplanned":
        score += 20

    return score