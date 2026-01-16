import matplotlib.pyplot as plt


def load_graph(past_prices: dict, stock_scenarios: dict) -> None:
    # Sort past prices by time
    past_prices_sorted = dict(sorted(past_prices.items()))
    past_y = list(past_prices_sorted.values())
    past_len = len(past_y)
    past_x = list(range(-past_len, 0))

    for model_name, data in stock_scenarios.items():
        plt.figure(figsize=(10, 6))

        # --- Plot past prices ---
        plt.plot(
            past_x,
            past_y,
            label="Past prices",
            linewidth=2.5,
            linestyle="-"
        )

        # --- Plot future scenarios ---
        scenarios = data["scenarios"]
        horizon_days = data["horizon_days"]
        future_x = list(range(horizon_days))

        for name, s in scenarios.items():
            plt.plot(
                future_x,
                s["prices"],
                label=f"{name.capitalize()} ({s['confidence']*100:.0f}%)"
            )

        # --- Decorations ---
        plt.axvline(0, linestyle="--", alpha=0.6, label="Now")
        plt.title(f"{data['ticker']} – Scenario Projection ({model_name})")
        plt.xlabel("Time (days)")
        plt.ylabel("Price")
        plt.legend()
        plt.grid(alpha=0.2)

        plt.show()