from fastapi import APIRouter
from reddit.models import Analysis

router = APIRouter()

@router.get("/results/{subreddit}")
def get_results(subreddit: str):
    try:
        analysis = Analysis.objects.filter(subreddit=subreddit).latest('timestamp')
        return {"subreddit": subreddit, "latest_analysis": analysis.summary}
    except Analysis.DoesNotExist:
        return {"error": "No analysis found for this subreddit"}
