# AI-Research-Assistant
AI Research Assistant (Python + LangChain + Gemini LLM + Research Tools) 


This project is an AI-powered research assistant built using LangChain, Google Gemini 2.5 Flash, and custom tool-augmented reasoning. It accepts any research query and generates a structured, machine-readable summary using a Pydantic schema:

1. What It Does
- Search the web using a custom `search_tool`
- Query Wikipedia using `wiki_tool`
- Process and structure information into a JSON response
- Save summaries automatically using `save_tool`
- Produce consistent output via Pydantic validation
- Store research results for later retrieval

2. Tech Stack
- Python
- LangChain Agents
- Pydantic v2
- Google Gemini 2.5 Flash
- Custom tools (search, wiki, save)
- dotenv for API key management

3. How It Works 
  1. User inputs a research question
  2. Agent determines topic & required sources
  3. Agent uses tools (`search_tool`, `wiki_tool`) to gather info
  4. LLM generates a structured JSON summary
  5. Output is validated using Pydantic
  6. Agent automatically calls `save_tool` to store the summary

Example Use Cases
- Quick research of academic topics
- High-level summaries for business or tech
- Structured dataset generation
- Automated report writing

