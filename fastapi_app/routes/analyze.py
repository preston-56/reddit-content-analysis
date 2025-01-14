from fastapi import APIRouter
from reddit.models import Analysis
from reddit_content_analysis.fetch import fetch_top_posts, analyze_posts

router = APIRouter()

@router.get("/analyze/{subreddit}")
def analyze_subreddit(subreddit: str):
    posts = fetch_top_posts(subreddit)
    analysis = analyze_posts(posts)

    # Save analysis to Django ORM
    Analysis.objects.create(subreddit=subreddit, summary=analysis)

    return {"message": "Analysis complete", "data": analysis}
