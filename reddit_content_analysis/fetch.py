import requests
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain_openai import OpenAI
from typing import List, Dict
from dotenv import load_dotenv
import os
from tenacity import retry, stop_after_attempt, wait_fixed

# Load environment variables
load_dotenv()

openai_api_key = os.getenv("OPENAI_API_KEY")
if not openai_api_key:
    raise EnvironmentError("OPENAI_API_KEY is not set in the environment variables.")

# Initialize the LLM
llm = OpenAI(temperature=0.7, model="gpt-3.5-turbo", openai_api_key=openai_api_key)


@retry(stop=stop_after_attempt(3), wait=wait_fixed(2))
def fetch_top_posts(subreddit: str, limit: int = 10) -> List[Dict]:
    """
    Fetch top posts from a given subreddit using Reddit's API.

    Args:
        subreddit (str): The subreddit to fetch posts from.
        limit (int): The number of top posts to fetch.

    Returns:
        List[Dict]: A list of dictionaries representing the top posts.
    """
    url = f"https://www.reddit.com/r/{subreddit}/top/.json?limit={limit}"
    headers = {"User-Agent": "RedditContentAnalysis/1.0"}

    try:
        response = requests.get(url, headers=headers, timeout=10)  # Added timeout
        response.raise_for_status()  # Raise HTTPError for bad responses (4xx, 5xx)
        posts = response.json().get("data", {}).get("children", [])
        return [
            {
                "title": post["data"]["title"],
                "score": post["data"]["score"],
                "content": post["data"].get("selftext", "")
            }
            for post in posts
        ]
    except requests.exceptions.RequestException as e:
        raise RuntimeError(f"Error fetching posts from subreddit {subreddit}: {str(e)}") from e


def analyze_posts(posts: List[Dict]) -> Dict:
    if not posts:
        return {"error": "No posts to analyze"}
    
    # Prepare content for LangChain analysis
    content = "\n".join([f"Title: {post['title']}\nContent: {post['content']}" for post in posts])

    # Define LangChain prompt
    template = """
    You are an expert in social media analysis. Analyze the given Reddit posts to identify:
    - Common patterns in post length, title structure, and posting times.
    - Key topics and themes discussed in the content.
    - Suggestions for creating successful posts.

    Reddit Posts:
    {content}

    Provide your analysis as a concise and clear summary.
    """
    prompt = PromptTemplate(input_variables=["content"], template=template)

    # Use LLMChain for chaining
    chain = LLMChain(llm=llm, prompt=prompt)

    try:
        langchain_summary = chain.run({"content": content})
    except Exception as e:
        # Handle insufficient quota error
        if "insufficient_quota" in str(e):
            langchain_summary = (
                "Error generating insights: You have exceeded your API quota. "
                "Please check your OpenAI plan and billing details."
            )
        else:
            langchain_summary = f"Error generating insights: {str(e)}"

    return {
        "total_posts": len(posts),
        "langchain_summary": langchain_summary,
    }
