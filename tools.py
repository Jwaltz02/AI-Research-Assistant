from langchain_community.tools import WikipediaQueryRun, DuckDuckGoSearchRun
from langchain_community.utilities import WikipediaAPIWrapper
from langchain.tools import tool
from datetime import datetime

@tool
def save_tool(text: str) -> str:
    """"save the research you just generated using save_tool"""
    filename = "research_output.txt"
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    formatted_text = f"--- Research Output ---\nTimestamp: {timestamp}\n\n{text}\n\n"

    with open(filename, "w", encoding="utf-8") as f:
        f.write(formatted_text)
    return f"Saved to {filename}"

search = DuckDuckGoSearchRun()

@tool
def search_tool(query: str) -> str:
    """search the web for information."""
    return search.run(query)

api_wrapper = WikipediaAPIWrapper(top_k_results=1, doc_content_chars_max=100)
wiki_tool = WikipediaQueryRun(api_wrapper=api_wrapper)

