import models_interface.models.chatgpt as chatgpt 


def fetch(ticker: str, current_price: float, horizon_days: int) -> dict:
    results = {}

    results['chatgpt'] = chatgpt.generate_stock_scenarios(
        ticker=ticker,
        current_price=current_price,
        horizon_days=horizon_days
    )

    # Placeholder for other models
    # results['gemini'] = gemini.generate_stock_scenarios(...)
    # results['llama'] = llama.generate_stock_scenarios(...)
    # results['mistral'] = mistral.generate_stock_scenarios(...)
    # results['claude'] = claude.generate_stock_scenarios(...)

    return results