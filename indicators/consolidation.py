def detect_consolidation(
        df,
        lookback=10,
        threshold=5):

    recent = df.tail(lookback)

    highest = recent["high"].max()

    lowest = recent["low"].min()

    consolidation_range = (
        (highest - lowest)
        / lowest
    ) * 100

    consolidating = (
        consolidation_range
        <= threshold
    )

    return (
        consolidating,
        consolidation_range
    )