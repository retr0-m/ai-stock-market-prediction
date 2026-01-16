import json, os
from anthropic import Anthropic
from dotenv import load_dotenv
import logs.log as log

logger = log.get_logger(name="claude", log_file="logs/outputs/claude.log")
load_dotenv()

client = Anthropic(api_key=os.getenv("CLAUDE_API_KEY"))

def generate_stock_scenarios(ticker, current_price, horizon_days=30, market="US"):
    log.info(logger, "Claude: generating stock scenarios")

    prompt = build_prompt(ticker, current_price, horizon_days, market)

    response = client.messages.create(
        model="claude-3-5-sonnet-latest",
        max_tokens=4000,
        temperature=0.4,
        messages=[{"role": "user", "content": prompt}]
    )

    return json.loads(response.content[0].text)