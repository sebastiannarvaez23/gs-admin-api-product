from fastapi import Path, Query, APIRouter
from fastapi.responses import JSONResponse
from typing import List
from src.models.candle_model import Candle, CandleCreate, CandleUpdate

candles: List[Candle] = []

candle_router = APIRouter()

@candle_router.get("/", tags=["Candles"])
def get_candles() -> List[Candle]:
    response = [candle.model_dump() for candle in candles]
    return JSONResponse(content=response, status_code=200)

@candle_router.get("/{id}", tags=["Candles"])
def get_candle(id: int = Path(gt=0)) -> Candle | dict:
    response: Candle = {}
    for candle in candles:
        if candle.id == id:
            response = candle.model_dump()
            return JSONResponse(content=response, status_code=200)
    return JSONResponse(content=response, status_code=404)

@candle_router.get("/by-name-and-by-wick", tags=["Candles"])
def get_candle_by_name_and_by_wick(
    name: str = Query(min_length=5, max_length=20), 
    wick: int = Query(ge=1, le=9)
    ) -> List[Candle]:
    
    response: List[Candle] = []
    for candle in candles:
        if name.lower() in candle.name.lower() and wick == candle.wick:
            response.candle_routerend(candle.model_dump())
    return JSONResponse(content=candle.model_dump(), status_code=200)

@candle_router.post("", tags=["Candles"])
def create_candle(candle: CandleCreate) -> Candle:
    candles.candle_routerend(candle)
    return JSONResponse(content=candle.model_dump(), status_code=201)

@candle_router.put("/{id}", tags=["Candles"])
def update_candle(id: int, candle: CandleUpdate) -> Candle:
    response: Candle = {}
    for cdl in candles:
        if cdl.id == id:
            cdl.name = candle.name
            cdl.price = candle.price
            cdl.cost = candle.cost
            cdl.wick = candle.wick
            response = candle.model_dump()
            return JSONResponse(content=response, status_code=200)
    return JSONResponse(content=response, status_code=404)

@candle_router.delete("/{id}", tags=["Candles"])
def delete_candle(id: int) -> Candle:
    response: Candle = {}
    for candle in candles:
        if candle.id == id:
            candleDeleted = candle.copy()
            response = candleDeleted.model_dump()
            candles.remove(candle)
            return JSONResponse(content=response, status_code=204)
    return JSONResponse(content=response, status_code=404)