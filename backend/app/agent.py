from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage
from langgraph.prebuilt import create_react_agent

from app.tools.drive_tool import drive_search_tool
from app.prompts.system_prompt import SYSTEM_PROMPT

import os
from dotenv import load_dotenv

load_dotenv()

llm = ChatOpenAI(
    model="openai/gpt-3.5-turbo",
    temperature=0,
    api_key=os.getenv("OPENROUTER_API_KEY"),
    base_url="https://openrouter.ai/api/v1"
)

agent = create_react_agent(
    llm,
    tools=[drive_search_tool]
)

async def run_agent(user_input: str):

    response = agent.invoke({
        "messages": [
            SystemMessage(content=SYSTEM_PROMPT),
            HumanMessage(content=user_input)
        ]
    })

    return response["messages"][-1].content
