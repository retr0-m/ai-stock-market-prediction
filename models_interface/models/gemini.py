import json
import os
import google.genai as genai
from dotenv import load_dotenv
import logs.log as log
from models_interface.parse_model_output import safe_parse_json

# Logger
logger = log.get_logger(name="gemini", log_file="logs/outputs/models/gemini.log")

# Load API key
load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
GEMINI_MODEL = "gemini-2.5-flash"

# Configure Gemini client
client = genai.Client(api_key=GEMINI_API_KEY)

def generate_stock_scenarios(prompt: str) -> dict:
    """
    Uses Google Gemini to generate structured future price scenarios
    suitable for plotting.
    """
    log.info(logger, "Generating stock scenarios using Gemini")

    try:
        # Generate content
        response = client.models.generate_content(
            model=GEMINI_MODEL, contents=prompt
        )



        # response.text contains the generated string
        result_text = response.text.strip()

        # Parse JSON safely
        result = safe_parse_json(result_text)
        log.info(logger, "Received valid JSON from Gemini")
        return result

    except json.JSONDecodeError as e:
        log.error(logger, f"Failed to parse Gemini JSON: {e}\nResponse: {response.text}")
        raise e
    except Exception as e:
        log.error(logger, f"Error generating stock scenarios: {e}")
        raise e
    
    
def run_prompt(client, prompt):
    """_summary_

    Args:
        client (gemini.client): Gemini client used for prompting
        prompt (str): prompt to be sent to the model

    Returns:
        website_content (str | None): generated website content if successful, None otherwise
    """
    log("prompting model for website...")
    try:
        response = client.models.generate_content(
            model=GEMINI_MODEL, contents=prompt
        )
        #!OUTDATED status_code = check_for_exeptions(response)
        return response.text

    except Exception as e:
        print(e)
        log("[FATAL ERROR]\tCould not generate website for the following reason: "+str(e))
        exception_page=handle_socket_genai_exception(e)
        log("Added exception to exception page template.")
        return exception_page

