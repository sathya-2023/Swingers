from core.universe_service import load_universe
from scanner.scanner_v1 import scan


stocks = load_universe("nifty50")

results = scan(stocks)

results = [
    stock
    for stock in results
    if stock["qualified"]
]

results = sorted(
    results,
    key=lambda x:
        x["final_score"],
    reverse=True
)

print()
print(
    f"Qualified Candidates: "
    f"{len(results)}"
)
print()

print()
print("=" * 70)

print(
    f"{'RANK':<6}"
    f"{'STOCK':<15}"
    f"{'FINAL':<10}"
    f"{'RS':<10}"
    f"{'BREAKOUT':<15}"
    f"{'RR':<10}"
)

print("=" * 70)

for i, stock in enumerate(results):

    print(
        f"{i+1:<6}"
        f"{stock['symbol']:<15}"
        f"{stock['final_score']:<10}"
        f"{round(stock['relative_strength'],2):<10}"
        f"{stock['breakout']['status']:<15}"
        f"{stock['trade_plan']['rr']:<10}"
    )
    
    
best = results[0]

print()
print("=" * 50)
print("BEST TRADE THIS WEEK")

top_results = results[:3]

for stock in top_results:

    print()
    print("=" * 50)

    print(stock["symbol"])

    print()

    print(
        "Entry:",
        stock["trade_plan"]["entry"]
    )

    print(
        "Stop:",
        stock["trade_plan"]["stop"]
    )

    print(
        "Target:",
        stock["trade_plan"]["target"]
    )

    print(
        "RR:",
        stock["trade_plan"]["rr"]
    )

    print(
        "Breakout:",
        stock["breakout"]["status"]
    )

    print(
        "Volume:",
        stock["volume_expansion"]["status"]
    )


# for stock in results:
#     # print()
#     # print("=" * 40)
    
#     # print(stock["symbol"],"= " , stock["current_price"])
#     # print(f"Score: {stock["score"]}")
#     # print(f"RS: {stock["relative_strength"]:.2f}")
    
#     # print(
#     #         "PASS"
#     #         if stock["qualified"]
#     #         else "FAIL"
#     # )
    
#     # print()
#     # print(f"52w High: {stock["high_52w"]:.2f}")
#     # print(f"Distance from 52w High: {stock["distance_52w"]:.2f}%")
    
#     # print()
    
#     # print("Strengths:")
#     # print(stock["strengths"])
    
#     # print()
    
#     # print("Weaknesses:")
#     # print(stock["weaknesses"])
#     # print()
    
#     # print(f"Consolidating: " 
#     #     f"{stock['consolidation_range']: .2f}%")




#     # print("\nConsolidation Details:")

#     # print(
#     #     "Support:",
#     #     stock["consolidation"]["support_price"]
#     # )

#     # print(
#     #     "Resistance:",
#     #     stock["consolidation"]["resistance_price"]
#     # )

#     # print(
#     #     "Candles:",
#     #     stock["consolidation"]["candles"]
#     # )

#     # print(
#     #     "Start:",
#     #     stock["consolidation"]["start_index"]
#     # )

#     # print(
#     #     "End:",
#     #     stock["consolidation"]["end_index"]
#     # )
    
#     # print("\nBreakout Details:")

#     # print(
#     #     "Resistance:",
#     #     stock["breakout"]["resistance_price"]
#     # )

#     # print(
#     #     "Current:",
#     #     stock["breakout"]["current_price"]
#     # )

#     # print(
#     #     "Distance:",
#     #     stock["breakout"]["distance"],
#     #     "%"
#     # )

#     # print(
#     #     "Status:",
#     #     stock["breakout"]["status"]
#     # )

#     # print(
#     #     "Score:",
#     #     stock["breakout"]["score"]
#     # )

#     # print(
#     #     "Pass:",
#     #     stock["breakout"]["passed"]
#     # )
    
    
#     # print("\nVolume Expansion:")

#     # print(
#     #     "Recent Volume:",
#     #     stock["volume_expansion"]["recent_volume"]
#     # )

#     # print(
#     #     "Average Volume:",
#     #     stock["volume_expansion"]["average_volume"]
#     # )

#     # print(
#     #     "Volume Ratio:",
#     #     stock["volume_expansion"]["volume_ratio"]
#     # )

#     # print(
#     #     "Status:",
#     #     stock["volume_expansion"]["status"]
#     # )

#     # print(
#     #     "Score:",
#     #     stock["volume_expansion"]["score"]
#     # )

#     # print(
#     #     "Confirmation:",
#     #     stock["volume_expansion"]["passed"]
#     # )
    
    
#     # print("\nTrade Plan:")

#     # print(
#     #     "Entry:",
#     #     stock["trade_plan"]["entry"]
#     # )

#     # print(
#     #     "Stop:",
#     #     stock["trade_plan"]["stop"]
#     # )

#     # print(
#     #     "Target:",
#     #     stock["trade_plan"]["target"]
#     # )

#     # print(
#     #     "Risk:",
#     #     stock["trade_plan"]["risk_pct"],
#     #     "%"
#     # )

#     # print(
#     #     "Reward:",
#     #     stock["trade_plan"]["reward_pct"],
#     #     "%"
#     # )

#     # print(
#     #     "RR:",
#     #     stock["trade_plan"]["rr"]
#     # )
#     # print(stock["symbol"], stock["final_score"])
    
#     print()
#     print("=" * 70)
#     print(
#         f"{'RANK':<6}"
#         f"{'STOCK':<15}"
#         f"{'FINAL':<10}"
#         f"{'RS':<10}"
#         f"{'BREAKOUT':<15}"
#         f"{'RR':<10}"
#     )
#     print("=" * 70)

#     for i, stock in enumerate(results):

#         print(
#             f"{i+1:<6}"
#             f"{stock['symbol']:<15}"
#             f"{stock['final_score']:<10}"
#             f"{round(stock['relative_strength'],2):<10}"
#             f"{stock['breakout']['status']:<15}"
#             f"{stock['trade_plan']['rr']:<10}"
#         )