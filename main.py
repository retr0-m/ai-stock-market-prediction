import logs.log as log
import models_interface.all_models as models
import stocks.get_stocks_prices as stocks
import output_processing.compare_predictions as compare
from output_processing.graphs.from_json import load_graph as graph_from_json
import output_processing.save_results as save_results
import config

logger = log.get_logger(name="main", log_file="logs/outputs/main.log")
log.info(logger, "Main module started.")

def main():
    for ticker in config.TICKERS:
        log.info(logger, f"Processing ticker: {ticker}")
        # fetching prices
        current_price = stocks.get_current_price(ticker)
        past_prices = stocks.get_historical_prices(ticker)

        # fetching model predictions
        stock_scenarios = models.fetch(
            ticker=ticker,
            current_price=current_price,
            horizon_days=30,
            past_prices=past_prices
        )
        
        # comparing predictions
        # compare.compare_models_predictions(stock_scenarios)
        graph_from_json(past_prices,stock_scenarios)
    
    # PIPELINE OF THE APPLICATION
    #       -> models_interface.chatgpt.py 
    #       -> models_interface.gemini.py
    #       -> models_interface.llama.py
    #       -> models_interface.mistral.py
    #       -> models_interface.claude.py
    #   then compare prices in output_processing/compare_predictions.py
    #   then save results in output_processing/save_results.py
    #   then visualize results in output_processing/graphs/from_json.py
    
if __name__ == "__main__":
    main()
    log.info(logger, "Main module finished.")