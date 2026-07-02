def calculate_final_score(stock):

    if not stock["qualified"]:
        return 0
    
    final_score = 0

    # Base score
    final_score += stock["score"]

    # Relative strength
    final_score += max(
        0,
        stock["relative_strength"]
    )

    # Breakout
    final_score += (
        stock["breakout"]["score"]
    )

    # Volume
    final_score += (
        stock["volume_expansion"]["score"]
    )

    # RR bonus
    rr = stock["trade_plan"]["rr"]

    if rr >= 2:
        final_score += 50

    elif rr >= 1.5:
        final_score += 30

    elif rr >= 1:
        final_score += 10

    return round(final_score, 2)