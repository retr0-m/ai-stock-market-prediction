# from stocks.get_stocks_prices import get_current_price

# def test_stocks_prices():
#     print(get_current_price("AAPL"))
#     print(get_current_price("BTC-USD"))


import logs.log as log

def test_logging():
    log.log_file_path = "logs/outputs/stocks.log"
    log.configure_logger(log_file=log.log_file_path)
    log.info("This is an info message.")
    log.warning("This is a warning message.")
    log.error("This is an error message.")

test_logging()




