from pathlib import Path
import logs.log as log

TEMPLATE_PATH = Path(__file__).parent / "prompt_template.txt"
logger= log.get_logger(name="prompt_builder", log_file="logs/outputs/prompt_builder.log")

def build_prompt(
    ticker: str,
    current_price: float,
    horizon_days: int,
    past_prices: dict,
    market: str = "US",
) -> str:
    """
    Load the prompt template and replace placeholders with values.
    """
    log.info(logger,"Building prompt for model")


    if not TEMPLATE_PATH.exists():
        log.error(logger, f"Prompt template not found at path: {TEMPLATE_PATH}")
        raise FileNotFoundError(f"Prompt template not found: {TEMPLATE_PATH}")

    template = TEMPLATE_PATH.read_text(encoding="utf-8")

    prompt = template.format(
        ticker=ticker,
        market=market,
        current_price=current_price,
        horizon_days=horizon_days,
        past_prices=past_prices
    )

    return prompt