from fastapi import APIRouter
from analyze.schemas.analyze import AnalyzeRequest, AnalyzeResponse
from analyze.models.analyze import analyze_text

router = APIRouter()

@router.post("/", response_model=AnalyzeResponse, summary="Analyze input text")
async def analyze(request: AnalyzeRequest) -> AnalyzeResponse:
    """
    Analyze the input text to generate a basic summary and sentiment.

    This endpoint receives a block of text and returns:
    - A brief summary (first 50 characters).
    - Sentiment polarity: positive, negative, or neutral.

    Args:
        request (AnalyzeRequest): Contains the input text.

    Returns:
        AnalyzeResponse: Contains the summary and sentiment result.
    """
    return analyze_text(request.text)
