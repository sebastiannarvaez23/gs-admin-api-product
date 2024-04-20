from fastapi import FastAPI
from src.routers.candle_router import candle_router

app = FastAPI()
app.title = "Garden Essence products managment."
app.version = "0.0.1"

app.include_router(prefix='/candle',router = candle_router)

# gt greater than
# ge greater than or equal
# lt less than
# le less than or equal