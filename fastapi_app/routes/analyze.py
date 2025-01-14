from fastapi import APIRouter, HTTPException
from reddit.models import Analysis
from reddit_content_analysis.fetch import fetch_top_posts, analyze_posts

router = APIRouter()

@router.get("/analyze/{subreddit}")
def analyze_subreddit(subreddit: str):
    # Fetch top posts from the specified subreddit
    posts = fetch_top_posts(subreddit)

    if not posts:
        raise HTTPException(status_code=404, detail="No posts found in subreddit")

    # Analyze the fetched posts
    analysis = analyze_posts(posts)

    # Check if analysis returned any error
    if "error" in analysis:
        raise HTTPException(status_code=500, detail=analysis["error"])

    # Save analysis to Django ORM (assuming `summary` is a JSON field or text field)
    Analysis.objects.create(subreddit=subreddit, summary=analysis)

    return {"message": "Analysis complete", "data": analysis}
