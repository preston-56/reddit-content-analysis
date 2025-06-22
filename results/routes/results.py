from fastapi import APIRouter
from results.models.results import fetch_analysis_results
from results.schemas.results import AnalysisResultsResponse

router = APIRouter()

@router.get("/", response_model=AnalysisResultsResponse, summary="Fetch Subreddit Analysis Results")
async def get_results():
    """
    Retrieve the latest subreddit analysis summaries.

    Returns:
        AnalysisResultsResponse: A structured list of subreddit analysis results.
    """
    results = fetch_analysis_results()
    return AnalysisResultsResponse(results=results)
