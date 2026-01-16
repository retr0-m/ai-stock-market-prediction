# models_interface/models/
import models_interface.models.chatgpt as chatgpt 
import models_interface.models.gemini as gemini
import models_interface.prompt_builder as prompt_builder
import models_interface.models.llava as llava
import logs.log as log
logger = log.get_logger(name="all_models", log_file="logs/outputs/all_models.log")

def fetch(
    ticker: str, 
    current_price: float, 
    horizon_days: int, 
    past_prices: dict
    ) -> dict:
    results = {}
    log.info(logger,f"Fetching stock scenarios for ticker: {ticker} using all models.")
    
    prompt = prompt_builder.build_prompt(ticker, current_price, horizon_days, past_prices=past_prices)
    results['chatgpt'] = chatgpt.generate_stock_scenarios(prompt)
    
    results['gemini'] = gemini.generate_stock_scenarios(prompt)
    results['llava'] = llava.generate_stock_scenarios(prompt)
    # results['mistral'] = mistral.generate_stock_scenarios(...)
    # results['claude'] = claude.generate_stock_scenarios(...)
    
    log.info(logger,f"Done fetching stock scenarios for ticker: {ticker}")

    return results