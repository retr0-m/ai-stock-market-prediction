import logs.log as log
import models_interface.all_models as models
import stocks.get_stocks_prices as stocks
import output_processing.compare_predictions as compare
from output_processing.graphs.from_json import load_graph as graph_from_json

log.configure_logger(log_file="logs/outputs/main.log")
log.info("Main module started.")

def main():
    current_price = stocks.get_current_price("AAPL")
    all_json_stock_scenarios = models.fetch(
        ticker="AAPL",
        current_price=current_price,
        horizon_days=30
    )
    graph_from_json(all_json_stock_scenarios)
    
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
    log.info("Main module finished.")