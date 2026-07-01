def detect_consolidation(
        df,
        lookback=10,
        threshold=5):

    recent = df.tail(lookback)

    resistance_price = recent["close"].max()
    support_price = recent["close"].min()

    consolidation_range = (
        (resistance_price - support_price)
        / support_price
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

        "support_price": support_price,

        "resistance_price": resistance_price
    }