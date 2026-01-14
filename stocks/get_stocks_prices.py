import yfinance as yf
import logs.log as log

log.configure_logger(log_file="logs/outputs/stocks.log")


def get_current_price(ticker: str) -> float:
    log.info(f"Fetching current price for ticker: {ticker}")
    try:
        stock = yf.Ticker(ticker)
    except Exception as e:
        log.error(f"Error fetching ticker data for {ticker}: {e}")
        log.info("Retrying to get current price due to error previous.")
    price = stock.fast_info["last_price"]
    log.info(f"Current price of AAPL: {float(price)}")
    return float(price)

def get_historical_prices(ticker: str, period: str = "1mo", interval: str = "1d"):
    log.info(f"Fetching historical prices for ticker: {ticker}, period: {period}, interval: {interval}")
    stock = yf.Ticker(ticker)
    hist = stock.history(period=period, interval=interval)
    return hist['Close'].tolist()
