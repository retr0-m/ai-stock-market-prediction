

def from_all_stock_scenarios(
        stock_scenarios: dict
    ) -> dict:
    comparison_results = {}

    for model_name, data in stock_scenarios.items():
        scenarios = data["scenarios"]
        model_comparison = {}

        for name, s in scenarios.items():
            final_price = s["prices"][-1]
            model_comparison[name] = {
                "final_price": final_price,
                "confidence": s["confidence"]
            }

        comparison_results[model_name] = model_comparison

    return comparison_results