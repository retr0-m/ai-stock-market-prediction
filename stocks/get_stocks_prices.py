import yfinance as yf

def get_current_price(ticker: str) -> float:
    stock = yf.Ticker(ticker)
    price = stock.fast_info["last_price"]
    return float(price)





from models_interface.chatgpt import generate_stock_scenarios

def get_stock_price_scenarios(
    ticker: str,
    horizon_days: int = 30,
    market: str = "US"
):
    current_price = get_current_price(ticker)
    scenarios_json = generate_stock_scenarios(
        ticker=ticker,
        current_price=current_price,
        horizon_days=horizon_days,
        market=market
    )
    return scenarios_json.py


