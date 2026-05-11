from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.agent import run_agent
from app.models.schemas import ChatRequest

app = FastAPI(title="Google Drive AI Assistant")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def health():
    return {"status": "ok"}

@app.post("/chat")
async def chat(req: ChatRequest):
    response = await run_agent(req.message)
    return {"response": response}