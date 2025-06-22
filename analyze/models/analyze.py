from textblob import TextBlob

def analyze_text(text: str) -> dict:
    """
    Perform a basic analysis of the given text, including:
    - A summary (first 50 characters with ellipsis).
    - Sentiment polarity: positive, negative, or neutral.

    Args:
        text (str): The text to analyze.

    Returns:
        dict: A dictionary containing the summary and sentiment.
    """
    summary = f"{text[:50]}..." if len(text) > 50 else text

    # Sentiment analysis using TextBlob
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    if polarity > 0.1:
        sentiment = "positive"
    elif polarity < -0.1:
        sentiment = "negative"
    else:
        sentiment = "neutral"

    return {
        "summary": summary,
        "sentiment": sentiment
    }
