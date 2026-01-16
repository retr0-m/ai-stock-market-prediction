from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
import logs.log as log

import stocks.get_stocks_prices as stocks
import models_interface.all_models as models

router = APIRouter()
logger = log.get_logger(name="api_routes", log_file="logs/outputs/api_routes.log")
# -------------------------
# Models
# -------------------------
class PredictionRequest(BaseModel):
    ticker: str
    horizon_days: int = 30
    market: str = "US"

# -------------------------
# Routes
# -------------------------
@router.get("/health")
async def health():
    return {"status": "ok"}

@router.get("/stocks/{ticker}/current")
async def current_price(ticker: str):
    try:
        return {
            "ticker": ticker,
            "price": stocks.get_current_price(ticker)
        }
    except Exception as e:
        log.error(logger, str(e))
        raise HTTPException(400, "Failed to fetch current price")

@router.get("/stocks/{ticker}/history")
async def history(
    ticker: str,
    period: str = "3mo",
    interval: str = "1d"
):
    try:
        return {
            "ticker": ticker,
            "period": period,
            "interval": interval,
            "prices": stocks.get_historical_prices(
                ticker,
                period=period,
                interval=interval
            )
        }
    except Exception as e:
        log.error(logger, str(e))
        raise HTTPException(400, "Failed to fetch historical data")


@router.post("/predict")
async def predict(req: PredictionRequest):
    try:
        current_price = stocks.get_current_price(req.ticker)
        past_prices = stocks.get_historical_prices(req.ticker)

        predictions = models.fetch(
            ticker=req.ticker,
            current_price=current_price,
            horizon_days=req.horizon_days,
            past_prices=past_prices
        )

        print("DEBUG predictions:", predictions)
        return {
            "ticker": req.ticker,
            "current_price": current_price,
            "horizon_days": req.horizon_days,
            "predictions": predictions
        }

    except Exception as e:
        log.error(logger, str(e))
        raise HTTPException(500, "Prediction failed")