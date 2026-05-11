# Google Drive Conversational AI Agent

## Features
- Conversational file search
- Google Drive API integration
- LangGraph agent
- Streamlit chat UI
- Natural language understanding

## Tech Stack
- FastAPI
- LangGraph
- OpenAI
- Streamlit
- Google Drive API

## Setup

### 1. Install Dependencies

Backend:
pip install -r backend/requirements.txt

Frontend:
pip install -r frontend/requirements.txt

### 2. Configure Environment Variables

Copy:
backend/.env.example

to:
backend/.env

### 3. Add Service Account Credentials

Place your JSON file inside:
credentials/service_account.json

### 4. Run Backend

cd backend
uvicorn app.main:app --reload

### 5. Run Frontend

cd frontend
streamlit run streamlit_app.py

## Deployment
- Backend: Railway / Render
- Frontend: Streamlit Cloud