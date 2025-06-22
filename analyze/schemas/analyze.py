from pydantic import BaseModel

class AnalyzeRequest(BaseModel):
    """
    Schema for the request body of the analyze endpoint.

    Attributes:
        text (str): The raw input text to be analyzed.
    """
    text: str

class AnalyzeResponse(BaseModel):
    """
    Schema for the response body of the analyze endpoint.

    Attributes:
        summary (str): A brief summary of the input text.
        sentiment (str): The sentiment polarity result — 'positive', 'neutral', or 'negative'.
    """
    summary: str
    sentiment: str
