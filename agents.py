import os
from dotenv import load_dotenv
from crewai import Agent
from langchain_openai import ChatOpenAI

load_dotenv()

os.environ["OPENAI_API_KEY"] = "your_api_key_here"

llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0.2
)

financial_analyst = Agent(
    role="Senior Financial Analyst",
    goal="Analyze financial documents and provide investment insights based on the query: {query}",
    verbose=True,
    memory=True,
    backstory=(
        "Experienced financial analyst with strong knowledge of markets, "
        "financial statements, and investment strategies."
    ),
    llm=llm,
    max_iter=2,
    allow_delegation=False
)
