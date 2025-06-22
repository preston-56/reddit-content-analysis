from fastapi import APIRouter, HTTPException
from generate.schemas.generate import SubredditInput, GeneratePostResponse
from generate.models.generate import build_langgraph

router = APIRouter()
graph = build_langgraph()

@router.post("/", response_model=GeneratePostResponse, summary="Generate a Reddit post suggestion")
async def generate_post_suggestion(state: SubredditInput):
    """
    Generate a Reddit post suggestion based on subreddit content analysis.

    - Accepts a subreddit name.
    - Uses LangGraph to analyze patterns and generate a sample post.
    - Returns the suggested post.
    """
    try:
        # Create initial state as dictionary for LangGraph
        initial_state = {"subreddit": state.subreddit}

        # Invoke the graph
        result = graph.invoke(initial_state)

        # Extract results from the final state
        return GeneratePostResponse(
            subreddit=result["subreddit"],
            suggested_post=result["post"]
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Post generation failed: {str(e)}")
