# from stocks.get_stocks_prices import get_current_price

# def test_stocks_prices():
#     print(get_current_price("AAPL"))
#     print(get_current_price("BTC-USD"))


import test
import logs.log as log

def test_logging():
    logger = log.get_logger(name="test",log_file=log.log_file_path)
    log.info(logger, "This is an info message.")
    log.warning(logger, "This is a warning message.")
    log.error(logger, "This is an error message.")


def test_past_data_fetching():
    from stocks.get_stocks_prices import get_historical_prices
    prices = get_historical_prices("AAPL", period="1mo", interval="1d")
    print(prices)
    return prices


import models_interface.prompt_builder as prompt_builder
def test_prompt_creation():
    prompt = prompt_builder.build_prompt(
        ticker="AAPL",
        current_price=150.0,
        horizon_days=30,
        past_prices=test_past_data_fetching()
    )
    return prompt
    print(prompt)
    
    
import models_interface.models.chatgpt as chatgpt
def test_chatgpt_integration():
    prompt = test_prompt_creation()
    response = chatgpt.generate_stock_scenarios(prompt)
    print(response)


import models_interface.models.gemini as gemini
def test_gemini_integration():
    prompt = test_prompt_creation()
    response = gemini.generate_stock_scenarios(prompt)
    print(response)

import models_interface.models.llava as llava
def test_llava_integration():
    prompt = test_prompt_creation()
    response = llava.generate_stock_scenarios(prompt)
    print(response)

test_llava_integration()
