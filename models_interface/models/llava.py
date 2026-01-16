import json
import logs.log as log
import requests

from models_interface.parse_model_output import parse_llava_output
# Logger
logger = log.get_logger(name="llava", log_file="logs/outputs/models/llava.log")

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "llava"


def generate_stock_scenarios(prompt: str) -> dict:
    """
    Uses Ollama llava to generate structured future price scenarios
    suitable for plotting.
    """
    log.info(logger, f"Generating stock scenarios using {MODEL_NAME}")

    try:
        # Send prompt to the model
        payload = {
            "model": MODEL_NAME,
            "prompt": prompt,
            "stream": False
        }
        
        response = requests.post(OLLAMA_URL, json=payload, timeout=120)
        response.raise_for_status()

        # The model response text
        result_text = parse_llava_output(response.text)

        # Parse JSON safely
        result = json.loads(result_text)
        log.info(logger, "Received valid JSON from llava")
        return result

    except json.JSONDecodeError as e:
        log.error(logger, f"Failed to parse JSON from llava: {e}\nResponse: {result_text}")
        raise e
    except Exception as e:
        log.error(logger, f"Error generating stock scenarios with llava: {e}")
        raise e
    
    
