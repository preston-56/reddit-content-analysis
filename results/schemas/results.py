from pydantic import BaseModel
from typing import List

class AnalysisResult(BaseModel):
    """
    Represents a single analysis result for a subreddit.

    Attributes:
        subreddit (str): The name of the analyzed subreddit.
        summary (str): A short summary of key discussion patterns.
        date (str): ISO-formatted timestamp when the analysis was generated.
    """
    subreddit: str
    summary: str
    date: str

class AnalysisResultsResponse(BaseModel):
    """
    Response model for returning multiple subreddit analysis results.

    Attributes:
        results (List[AnalysisResult]): A list of individual analysis results.
    """
    results: List[AnalysisResult]
