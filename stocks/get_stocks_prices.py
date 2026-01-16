import yfinance as yf
import logs.log as log
from config import DEFAULT_PAST_DATA_INTERVAL, DEFAULT_PAST_DATA_PERIOD

logger = log.get_logger(name="stocks", log_file="logs/outputs/stocks.log")


def get_current_price(ticker: str) -> float:
    log.info(logger, f"Fetching current price for ticker: {ticker}")
    try:
        stock = yf.Ticker(ticker)
    except Exception as e:
        log.error(logger, f"Error fetching ticker data for {ticker}: {e}")
        log.info(logger, "Retrying to get current price due to error previous.")
    price = stock.fast_info["last_price"]
    log.info(logger, f"Current price of AAPL: {float(price)}")
    return float(price)

def get_historical_prices(
    ticker: str,
    period: str = DEFAULT_PAST_DATA_PERIOD,
    interval: str = DEFAULT_PAST_DATA_INTERVAL
) -> dict:
    log.info(logger,
        f"Fetching historical prices for ticker: {ticker}, "
        f"period: {period}, interval: {interval}"
    )

    stock = yf.Ticker(ticker)
    hist = stock.history(period=period, interval=interval)
    hist = hist.tz_convert("UTC")

    if hist.empty:
        log.warning(logger,f"No historical data returned for {ticker}")
        return {}

    prices = {
        idx.strftime("%Y-%m-%d %H:%M UTC"): float(price)
        for idx, price in hist["Close"].items()
    }


    return prices