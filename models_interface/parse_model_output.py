import re
import json
import logs.log as log

logger = log.get_logger("parse_model_output", "logs/outputs/parse_model_output.log")

def safe_parse_json(text: str):
    """
    Tries to extract the first {...} block and parse it as JSON.
    Works around AI models that append extra characters.
    """
    # Remove leading/trailing whitespace
    text = text.strip()

    # Match first { ... } block
    match = re.search(r"\{.*\}", text, re.DOTALL)
    if match:
        try:
            return json.loads(match.group(0))
        except json.JSONDecodeError as e:
            raise ValueError(f"Failed to parse repaired JSON: {e}\nOriginal text: {text}")
    else:
        raise ValueError(f"No JSON object found in text: {text}")
    

def parse_llava_output(llava_response: dict) -> dict:
    """
    Extracts the valid JSON from the Llama response.
    Handles cases where the model returns extra keys or prepends weird chars.
    """
    try:
        # llava_response['response'] contains the text output
        text = llava_response.get("response", "")
        if not text:
            raise ValueError("No 'response' in llava output")

        # Clean up common issues: remove leading extra quotes/whitespace
        text = text.strip()
        text = re.sub(r'^"+\s*', '', text)  # remove leading quotes
        text = re.sub(r'\s*"+$', '', text)  # remove trailing quotes

        # Extract first {...} block
        match = re.search(r"\{.*\}", text, re.DOTALL)
        if not match:
            raise ValueError(f"No JSON object found in Llama output: {text}")

        # Parse JSON
        result = json.loads(match.group(0))

        # Convert any numpy floats to Python floats
        for scenario in ["bull", "base", "bear"]:
            prices = result["scenarios"][scenario]["prices"]
            result["scenarios"][scenario]["prices"] = [float(p) for p in prices]

        return result

    except Exception as e:
        log.error(logger, f"Failed to parse Llama output: {e}")
        raise