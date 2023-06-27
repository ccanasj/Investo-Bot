from pydantic import BaseModel
from datetime import date


class PredictResponse(BaseModel):
    dates: list[date]
    
    closing_price: list[float]
    predicted_closing_price: list[float]