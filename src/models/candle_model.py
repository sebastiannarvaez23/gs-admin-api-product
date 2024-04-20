from pydantic import BaseModel, Field
from typing import Optional

class Candle(BaseModel):
    id: int
    name: str
    price: float
    cost: float
    wick: str
    scent: Optional[str] = None
    pass

class CandleCreate(BaseModel):
    id: int
    name: str = Field(min_length=10, max_length=100)
    price: float = Field(ge=3, le=6)
    cost: float = Field(ge=3, le=6)
    wick: str = Field(min_length=1, max_length=1, default="1")
    scent: Optional[str] = None
    
    model_config = {
        "json_schema_extra": {
            "example": {
                "id": 1,
                "name": "Mi nueva vela",
                "price": 7000,
                "cost": 1800,
                "wick": "2",
                "scent": "Vainilla" 
            }
        }
    }
    pass

class CandleUpdate(BaseModel):
    name: str
    price: float
    cost: float
    wick: str
    scent: Optional[str] = None
    pass