from fastapi import APIRouter, HTTPException
import openai
import os
from pydantic import BaseModel
class GenerateRequest(BaseModel):
    subreddit: str

router = APIRouter()

COMPOSIO_API_KEY = os.getenv("COMPOSIO_API_KEY")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

if not COMPOSIO_API_KEY or not OPENAI_API_KEY:
    raise EnvironmentError("API keys for OpenAI are not set in the environment variables.")

openai.api_key = OPENAI_API_KEY

@router.post("/generate")
async def generate_post_suggestions(request: GenerateRequest):
    try:
        # Extract subreddit from request
        subreddit = request.subreddit

        # Define direct mock analysis results
        analysis_results = {
            "python": "Posts in the 'python' subreddit are often technical, contain code snippets, and focus on learning and collaboration.",
            "learnprogramming": "Posts in 'learnprogramming' are usually questions about coding problems, advice on learning resources, and beginner-friendly."
        }.get(subreddit)

        if not analysis_results:
            raise HTTPException(status_code=404, detail="No analysis results found for this subreddit")

        # Construct the prompt for OpenAI
        prompt = f"Based on the following analysis results for subreddit '{subreddit}', create a Reddit post that aligns with successful patterns:\n\n{analysis_results}"

        # Request OpenAI to generate a post using the new API method
        response = await openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=1000,
            temperature=0.7
        )

        # Extract generated post from OpenAI response
        generated_post = response['choices'][0]['message']['content'].strip()

        return {"generated_post": generated_post}

    except HTTPException as http_err:
        raise http_err from None
    except Exception as err:
        raise HTTPException(status_code=500, detail=f"An error occurred: {str(err)}") from err
