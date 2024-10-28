
import os
from dotenv import load_dotenv

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_core.chat_history import (
    BaseChatMessageHistory,
    InMemoryChatMessageHistory,
)
from langchain_community.callbacks import get_openai_callback


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SYS_PROMPT_PATH = os.path.join(
    BASE_DIR, "sys_prompts", "system_prompt1.txt"
)

load_dotenv(override=True)
app = FastAPI()

# Initializing chatHistory
store = {}


def get_session_history(session_id: str) -> BaseChatMessageHistory:
    """Get the chat message history for a given session ID.

    Args:
        session_id (str): The session ID.

    Returns:
        BaseChatMessageHistory: The chat message history for the session.
    """
    if session_id not in store:
        store[session_id] = InMemoryChatMessageHistory()
    return store[session_id]


# Initialize AzureChatOpenAI LLM
model = ChatOpenAI(
model="gpt-3.5-turbo"
)

# Read System Prompt from File and remove special characters
with open(SYS_PROMPT_PATH, "r", encoding="utf-8") as file_systeminput:
    system_prompt = file_systeminput.read()
    #system_prompt = remove_special_characters(system_prompt)

# Prompt Template
prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            system_prompt,
        ),
        MessagesPlaceholder(variable_name="messages"),
    ]
)

chain = prompt | model
llm_with_history = RunnableWithMessageHistory(chain, get_session_history)


class PalletizerRequest(BaseModel):

    user_input: str
    session_id: str


@app.post("/palletize")
async def palletizer_request(request: PalletizerRequest) -> dict:
    """Invokes the Azure Chat OpenAI model with the given user input.

    Args:
        request (PalletizerRequest): The request payload containing the user input and session ID.

    Returns:
        dict: The response JSON containing the session ID, user input, generated response, and chat history.
    """
    try:
        chat_history = get_session_history(request.session_id)
        user_input = request.user_input
        session = {"configurable": {"session_id": request.session_id}}
        with get_openai_callback() as cb:
            response = llm_with_history.invoke(
                user_input,
                config=session,
            )

        history = []

        # Add the user input and the response to the chat history
        for msg in chat_history.messages:
            history.append(msg.content)

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e)) from e

    return {
        "session_id": request.session_id,
        "user_input": user_input,
        "response": response.content,
        "history": history,
    }


if __name__ == "__main__":
    import uvicorn

    load_dotenv(override=True)
    uvicorn.run(app, host="0.0.0.0", port=int(os.environ["API_PORT"]))
