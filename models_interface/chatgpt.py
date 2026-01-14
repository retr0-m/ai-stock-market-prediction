import json
from openai import OpenAI

client = OpenAI()

def generate_stock_scenarios(
    ticker: str,
    current_price: float,
    horizon_days: int = 30,
    market: str = "US"
):
    """
    Uses ChatGPT to generate structured future price scenarios
    suitable for plotting.
    """

    prompt = f"""
    You are a quantitative market analyst.

    Generate plausible future price scenarios for the stock below.
    This is NOT financial advice or a real prediction — it is a
    scenario-based projection for visualization purposes.

    Stock ticker: {ticker}
    Market: {market}
    Current price: {current_price}
    Time horizon: {horizon_days} days

    Rules:
    - Output ONLY valid JSON
    - Prices must be floats
    - Each scenario must have exactly {horizon_days} values
    - Ensure smooth daily transitions (no extreme jumps)
    - Bull, Base, Bear confidence must sum to 1.0
    - Use realistic volatility based on market conditions and future events
    - Consider macroeconomic factors, sector trends, and company performance
    
    Output:
    - Give only the JSON object as described below, no introduction test, nothing, just the JSON.

    JSON format:
    {{
        "ticker": "...",
        "currency": "...",
        "horizon_days": {horizon_days},
        "assumptions": {{
        "volatility_level": "low | medium | high",
        "trend_bias": "bullish | neutral | bearish"
        }},
        "scenarios": {{
        "bull": {{
            "confidence": 0.0,
            "prices": []
        }},
        "base": {{
            "confidence": 0.0,
            "prices": []
        }},
        "bear": {{
            "confidence": 0.0,
            "prices": []
        }}
    }}
    }}
    """

    response = client.chat.completions.create(
        model="gpt-4.1",
        messages=[
            {"role": "system", "content": "You generate market scenario data for visualization."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.4
    )

    return json.loads(response.choices[0].message.content)


if __name__ == "__main__":
    data = generate_stock_scenarios(
        ticker="AAPL",
        current_price=195.0,
        horizon_days=30
    )

    print(json.dumps(data, indent=2))