import matplotlib.pyplot as plt
import json




def load_graph(all_json_stock_scenarios: dict):
    for model_name, data in all_json_stock_scenarios.items():
        plt.figure(figsize=(10, 6))
        scenarios = data["scenarios"]

        for name, s in scenarios.items():
            plt.plot(s["prices"], label=f"{name} ({s['confidence']*100:.0f}%)")

        plt.title(f"{data['ticker']} – Scenario Projection by {model_name}")
        plt.xlabel("Days")
        plt.ylabel("Price")
        plt.legend()
        plt.show()
        input("Press Enter to continue...")