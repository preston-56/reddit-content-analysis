import requests
from typing import List, Dict

# Fetch top posts from a subreddit using the Reddit JSON API
def fetch_top_posts(subreddit_name: str, limit: int = 20) -> List[Dict]:
    """
    Fetches the top posts from a given subreddit.
    
    Args:
        subreddit_name (str): The name of the subreddit to fetch posts from.
        limit (int): The number of posts to fetch. Defaults to 20.
        
    Returns:
        List[Dict]: A list of dictionaries containing the top post details.
    """
    url = f"https://www.reddit.com/r/{subreddit_name}/top.json"
    headers = {"User-Agent": "RedditContentAnalysis/1.0"}
    
    try:
        response = requests.get(url, headers=headers, params={"limit": limit})
        response.raise_for_status()  # Raise an HTTPError for bad responses (4xx and 5xx)
        data = response.json()
        
        posts = []
        for item in data["data"]["children"]:
            post = {
                "title": item["data"]["title"],
                "author": item["data"]["author"],
                "score": item["data"]["score"],
                "created_utc": item["data"]["created_utc"],
                "num_comments": item["data"]["num_comments"],
                "permalink": item["data"]["permalink"],
                "content": item["data"].get("selftext", ""),  # Post text (if any)
            }
            posts.append(post)
        
        return posts

    except requests.exceptions.RequestException as e:
        print(f"Error fetching top posts: {e}")
        return []

def analyze_posts(posts: List[Dict]) -> Dict:
    """
    Analyze the given list of posts to find common patterns.
    
    Args:
        posts (List[Dict]): A list of dictionaries representing posts.
        
    Returns:
        Dict: A summary of the analysis.
    """
    if not posts:
        return {"error": "No posts to analyze"}
    
    # Example analysis: Calculate average title length, post score, etc.
    total_title_length = sum(len(post["title"]) for post in posts)
    total_score = sum(post["score"] for post in posts)
    average_title_length = total_title_length / len(posts)
    average_score = total_score / len(posts)

    # Extract common words in titles
    from collections import Counter
    all_words = " ".join(post["title"] for post in posts).split()
    common_words = Counter(all_words).most_common(5)

    # Generate summary
    summary = {
        "total_posts": len(posts),
        "average_title_length": average_title_length,
        "average_score": average_score,
        "common_words_in_titles": [word for word, _ in common_words],
    }
    
    return summary
