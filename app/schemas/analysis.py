from pydantic import BaseModel
from typing import List


class New(BaseModel):
    title: str
    link: str


class AnalysisResponse(BaseModel):

    emotion: str

    positive_percentage: float
    neutral_percentage: float
    negative_percentage: float

    news: List[New]
