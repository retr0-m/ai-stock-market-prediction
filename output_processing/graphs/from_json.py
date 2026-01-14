import matplotlib.pyplot as plt
import json
def load_graph(json_data_path: str):
    with open(json_data_path, 'r') as f:
        data = json.load(f)
        
    scenarios = data["scenarios"]

    for name, s in scenarios.items():
        plt.plot(s["prices"], label=f"{name} ({s['confidence']*100:.0f}%)")

    plt.title(f"{data['ticker']} – Scenario Projection")
    plt.xlabel("Days")
    plt.ylabel("Price")
    plt.legend()
    plt.show()