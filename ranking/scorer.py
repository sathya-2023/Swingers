def score(analysis):

    points = 0

    if analysis["above_ema50"]:
        points += 25

    if analysis["above_ema200"]:
        points += 25

    if analysis["weekly_return"] > 0:
        points += 25

    if analysis["monthly_return"] > 0:
        points += 25

    return points