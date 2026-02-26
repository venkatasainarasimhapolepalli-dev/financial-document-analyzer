import os
from crewai.tools import tool
from pypdf import PdfReader


@tool("Read Financial Document")
def read_data_tool(file_path: str) -> str:
    """Reads a PDF financial document and returns text"""

    if not os.path.exists(file_path):
        return "File not found."

    try:
        reader = PdfReader(file_path)
        text = ""

        for page in reader.pages:
            if page.extract_text():
                text += page.extract_text()

        return text[:4000]

    except Exception as e:
        return f"Error reading file: {str(e)}"


@tool("Financial Analyzer Tool")
def financial_tool(query: str) -> str:
    """Simple financial analysis helper"""
    return f"Analyzing financial query: {query}"
