from fastapi import FastAPI, File, UploadFile, Form, HTTPException
import os
import uuid

from crewai import Crew, Process
from agents import financial_analyst
from task import analyze_financial_document as analyze_task

app = FastAPI(title="Financial Document Analyzer")


def run_crew(query: str):
    financial_crew = Crew(
        agents=[financial_analyst],
        tasks=[analyze_task],
        process=Process.sequential,
    )

    result = financial_crew.kickoff({"query": query})
    return result


@app.get("/")
async def root():
    return {"message": "Financial Document Analyzer API is running"}


@app.post("/analyze")
async def analyze_endpoint(
    file: UploadFile = File(...),
    query: str = Form(default="Analyze this financial document"),
):
    file_id = str(uuid.uuid4())
    file_path = f"data/financial_document_{file_id}.pdf"

    try:
        os.makedirs("data", exist_ok=True)

        with open(file_path, "wb") as f:
            content = await file.read()
            f.write(content)

        response = run_crew(query=query)

        return {
            "status": "success",
            "analysis": str(response),
            "file": file.filename
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

    finally:
        if os.path.exists(file_path):
            os.remove(file_path)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
