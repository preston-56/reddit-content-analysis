from results.schemas.results import AnalysisResult
from datetime import datetime
from typing import List

# Simulated data source (e.g., could be replaced with DB access logic later)
def fetch_analysis_results() -> List[AnalysisResult]:
    """
    Fetch a list of recent subreddit analysis summaries.

    Returns:
        List[AnalysisResult]: A list of analysis results including subreddit name, summary, and timestamp.
    """
    return [
        AnalysisResult(
            subreddit="python",
            summary="Discussions often center around asynchronous programming, web frameworks like FastAPI and Django, and packaging tools like Poetry.",
            date=datetime.now().isoformat()
        ),
        AnalysisResult(
            subreddit="learnprogramming",
            summary="Frequent posts include beginner questions about syntax, career advice, debugging help, and study resources.",
            date=datetime.now().isoformat()
        )
    ]
