from langgraph.graph import StateGraph, END
from langchain_core.runnables import Runnable
from generate.schemas.generate import SubredditState
from typing import Dict, Any

def analyze_subreddit(state: Dict[str, Any]) -> Dict[str, Any]:
    """Analyze a subreddit and return updated state."""
    analysis_map = {
        "python": (
            "Posts in 'python' are technical, often include code examples, "
            "library recommendations, and discussions on best practices."
        ),
        "learnprogramming": (
            "Posts in 'learnprogramming' are beginner-focused, including debugging help, "
            "learning resources, and conceptual explanations."
        )
    }

    # Access dictionary keys
    analysis = analysis_map.get(state["subreddit"], "No analysis available for this subreddit.")

    # Return partial state update
    return {"analysis": analysis}

def generate_post_using_analysis(state: Dict[str, Any]) -> Dict[str, Any]:
    """Generate a Reddit post suggestion using the previous analysis result."""
    post = (
        "Here's a post suggestion:\n\n"
        f"{state['analysis']}\n\n"  # Access dictionary keys
        "Does this reflect what works well in that subreddit?"
    )

    # Return partial state update
    return {"post": post}

def build_langgraph() -> Runnable:
    """Builds and compiles the LangGraph using typed state."""
    graph = StateGraph(SubredditState)

    graph.add_node("analyze", analyze_subreddit)
    graph.add_node("generate", generate_post_using_analysis)

    graph.set_entry_point("analyze")
    graph.add_edge("analyze", "generate")
    graph.add_edge("generate", END)

    return graph.compile()
