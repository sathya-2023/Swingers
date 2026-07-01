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

    start_index = len(df) - lookback
    end_index = len(df) - 1

    return {
        "consolidating": consolidating,

        "range_pct": round(
            consolidation_range,
            2
        ),

        "candles": lookback,

        "start_index": start_index,

        "end_index": end_index,

        "support": lowest,

        "resistance": highest
    }