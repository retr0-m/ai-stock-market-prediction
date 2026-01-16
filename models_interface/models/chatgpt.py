import json
from openai import OpenAI
from dotenv import load_dotenv
import os
import logs.log as log
from models_interface.parse_model_output import safe_parse_json

logger = log.get_logger(name="chatgpt", log_file="logs/outputs/chatgpt.log")

load_dotenv()
CHATGPT_API_KEY = os.getenv("CHATGPT_API_KEY")

client = OpenAI(api_key=CHATGPT_API_KEY)


def generate_stock_scenarios(prompt: str) -> dict:
    """
    Uses ChatGPT to generate structured future price scenarios
    suitable for plotting.
    """
    log.info(logger, "Generating stock scenarios using ChatGPT")
    try:
        response = client.chat.completions.create(
            model="gpt-4.1",
            messages=[
                {"role": "system", "content": "You generate market scenario data for visualization."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.4
        )
        result = safe_parse_json(response.choices[0].message.content)

        return result
    except json.JSONDecodeError as e:
        log.error(logger, f"Failed to parse ChatGPT JSON: {e}\nResponse: {response.text}")
        raise e
    except Exception as e:
        log.error(logger, f"Error generating stock scenarios: {e}")
        raise e

