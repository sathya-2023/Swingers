def score(analysis):

    points = 0

    # Trend
    if analysis["above_ema50"]:
        points += 25

    if analysis["above_ema200"]:
        points += 25

    # Weekly momentum
    weekly = analysis["weekly_return"]

    if weekly > 5:
        points += 25
    elif weekly > 3:
        points += 20
    elif weekly > 1:
        points += 10
    elif weekly > 0:
        points += 5

    # Monthly momentum
    monthly = analysis["monthly_return"]

    if monthly > 15:
        points += 25
    elif monthly > 10:
        points += 20
    elif monthly > 5:
        points += 10
    elif monthly > 0:
        points += 5

    return points