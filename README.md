# Financial Document Analyzer — Debug Assignment

## 📌 Project Overview

This project is an AI-powered financial document analysis system that processes corporate reports, financial statements, and investment documents using CrewAI agents and FastAPI.

The objective of this assignment was to debug the provided broken codebase, resolve dependency and architectural issues, and deliver a fully working backend API.

---

## 🚀 Features

* Upload financial documents (PDF)
* AI-powered financial analysis
* Investment insights
* Risk assessment
* FastAPI backend
* CrewAI agent orchestration

---

## 🐛 Bugs Identified and Fixes

During debugging, several critical issues were found and fixed:

### 1. Missing Dependencies

**Issue**

```
ModuleNotFoundError: No module named 'langchain_openai'
```

**Fix**

Installed required packages and aligned versions in `requirements.txt`.

---

### 2. Circular Imports in tools.py

**Issue**

```
ImportError: partially initialized module 'tools'
```

Cause: File was importing itself.

**Fix**

Removed:

```python
from tools import read_data_tool, financial_tool
```

Defined tools directly inside the file.

---

### 3. Undefined Variables

**Issue**

```
NameError: financial_tool is not defined
```

**Fix**

Created and exported `financial_tool` properly in `tools.py` and imported in `task.py`.

---

### 4. Incorrect Tool Import

**Issue**

```
from crewai_tools import tool
```

Not valid for current CrewAI version.

**Fix**

Changed to:

```python
from crewai.tools import tool
```

---

### 5. Missing API Key Configuration

**Issue**

Project expected `.env` file but none provided.

**Fix**

Added direct environment variable support:

```python
import os
os.environ["OPENAI_API_KEY"] = "your_api_key"
```

---

### 6. Agent Import Errors

**Issue**

Verifier agent referenced but not defined.

**Fix**

Removed invalid imports and simplified agent structure.

---

### 7. File Handling Logic

Improved temporary file handling and cleanup logic in `main.py`.

---

## 📂 Project Structure

```
financial-document-analyzer/
│
├── main.py              # FastAPI server
├── agents.py            # CrewAI agent definitions
├── task.py              # Task definitions
├── tools.py             # Custom tools
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation

### 1. Clone Repository

```bash
git clone <your-repo-url>
cd financial-document-analyzer
```

### 2. Create Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate   # Windows
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Setup

Set your OpenAI API key:

Windows PowerShell:

```bash
setx OPENAI_API_KEY "your_api_key_here"
```

Or inside code (for testing only):

```python
os.environ["OPENAI_API_KEY"] = "your_api_key_here"
```

---

## ▶️ Running the Application

```bash
python main.py
```

Server will start at:

```
http://localhost:8000
```

Swagger UI:

```
http://127.0.0.1:8000/docs
```

---

## 📡 API Documentation

### GET /

Health check endpoint.

Response:

```json
{
  "message": "Financial Document Analyzer API is running"
}
```

---

### POST /analyze

Upload a financial document for analysis.

#### Form Data

| Field | Type   | Required |
| ----- | ------ | -------- |
| file  | PDF    | Yes      |
| query | string | No       |

#### Example Response

```json
{
  "status": "success",
  "analysis": "Financial insights...",
  "file": "sample.pdf"
}
```

---

## 🧠 Technologies Used

* FastAPI
* CrewAI
* LangChain OpenAI
* Python
* PDF Processing (pypdf)

---

## 🎯 Assignment Objective

This project demonstrates:

* Debugging skills
* Dependency management
* Backend development
* AI agent orchestration
* Problem solving ability