from crewai import Task
from agents import financial_analyst
from tools import read_data_tool, financial_tool   


analyze_financial_document = Task(
    description="Analyze the financial document based on the user query: {query}",
    expected_output="Financial insights",
    agent=financial_analyst,
    tools=[read_data_tool],
    async_execution=False,
)


investment_analysis = Task(
    description="Provide investment analysis based on financial data. Query: {query}",
    expected_output="Investment recommendations",
    agent=financial_analyst,
    tools=[read_data_tool],
    async_execution=False,
)


risk_assessment = Task(
    description="Provide risk assessment based on financial data. Query: {query}",
    expected_output="Risk analysis",
    agent=financial_analyst,
    tools=[read_data_tool],
    async_execution=False,
)


verification = Task(
    description="Verify whether the uploaded file is a financial document.",
    expected_output="Verification result",
    agent=financial_analyst,
    tools=[financial_tool],   
    async_execution=False,
)
