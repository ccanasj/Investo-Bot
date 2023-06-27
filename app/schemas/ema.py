from pydantic import BaseModel
from datetime import date
from typing import Any


class EMAResponse(BaseModel):
    action: str
    
    dates: list[date]
    
    ema_short: list[float]
    ema_long: list[float]
    closing_price: list[int]
    

class HistoryResponse(BaseModel):
    history: dict[str, dict[date, float]]
    

class InfoResponse(BaseModel):
    info: dict[str, Any]
