from dotenv import load_dotenv
from pydantic import BaseModel
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from langchain.agents import create_agent
from langchain.tools import tool 
from tools import search_tool, wiki_tool, save_tool

load_dotenv()

class ResearchResponse(BaseModel):
    topic: str
    summary: str
    sources: list[str]
    tools_used: list[str]

llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

parser = PydanticOutputParser(pydantic_object=ResearchResponse)

system_prompt = """
You are a research assistant that helps generate structured research summaries.

Given a user query, you will:
- Identify the topic
- Provide a concise but useful summary
- List the sources you relied on (as strings)
- List any tools you used (as strings)
- Return ONLY JSON that matches this schema: {format_instructions}
- After producing the JSON, ALWAYS call save_tool and ONLY pass the summary to it.


""".strip().format(format_instructions=parser.get_format_instructions())

tools = [search_tool, wiki_tool, save_tool]

agent = create_agent(
    model=llm,
    tools=tools,
    system_prompt=system_prompt,
)

query = input("What can I help you research? ")

result_state = agent.invoke(
    {
        "messages": [
            {"role": "user", "content": query}
        ]
    }
)

# The agent returns a state dict with a "messages" list; last message is the final reply
final_message = result_state["messages"][-1].content
if isinstance(final_message, list):
    final_message = "".join([x.get("text", "") if isinstance(x, dict) else str(x) for x in final_message])

parsed_response = parser.parse(final_message)
print(parsed_response)

try:
    parsed_response = parser.parse(final_message)
except Exception as e:
    print("Error parsing response", e, "Raw response -", parsed_response)

