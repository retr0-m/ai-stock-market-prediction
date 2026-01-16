from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

import logs.log as log
from server.api.routes import router as api_router

logger = log.get_logger(
    name="server",
    log_file="logs/outputs/server.log"
)

app = FastAPI(
    title="Stock Scenario API",
    version="1.0.0"
)

# -------------------------
# Static & templates
# -------------------------
app.mount("/static", StaticFiles(directory="server/static"), name="static")
templates = Jinja2Templates(directory="server/templates")

# -------------------------
# Dashboard
# -------------------------
@app.get("/")
async def dashboard(request: Request):
    log.info(logger, "Serving dashboard")
    return templates.TemplateResponse(
        "index.html",
        {"request": request}
    )

# -------------------------
# API
# -------------------------
app.include_router(api_router, prefix="/api")