from fastapi import APIRouter
from app.ia import getInfo, get_emotions
from app.schemas import AnalysisResponse


analysis_router = APIRouter(prefix="/api/v1/analysis",
                            tags=["Sentiment Analysis"])


@analysis_router.get("/{symbol}/emotions", response_model=AnalysisResponse)
async def emotions(symbol: str):

    name = getInfo(symbol).get("longName")
    positive_percentage, neutral_percentage, negative_percentage, top_news = get_emotions(name)
    
    if positive_percentage >= neutral_percentage and positive_percentage >= negative_percentage:
        emotion = "positive"
    elif neutral_percentage >= positive_percentage and neutral_percentage >= negative_percentage:
        emotion = "neutral"
    else:
        emotion = "negative"

    return {
        "emotion": emotion,
        "positive_percentage": positive_percentage,
        "neutral_percentage": neutral_percentage,
        "negative_percentage": negative_percentage,
        "news": top_news
    }
