from pydantic import BaseModel
from typing import Optional
from typing_extensions import TypedDict

class SubredditInput(BaseModel):
    """
    Input schema for post generation. Represents the user's request payload.
    """
    subreddit: str

class SubredditState(TypedDict):
    """
    LangGraph state schema - use TypedDict for better LangGraph compatibility.
    """
    subreddit: str
    analysis: Optional[str]
    post: Optional[str]

class GeneratePostResponse(BaseModel):
    """
    Output schema returned to the user after post generation.
    """
    subreddit: str
    suggested_post: str