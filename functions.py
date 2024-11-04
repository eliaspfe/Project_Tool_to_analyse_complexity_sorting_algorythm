
import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.chat_history import (
    BaseChatMessageHistory,
    InMemoryChatMessageHistory,
)
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.runnables.history import RunnableWithMessageHistory

# Path to the system prompt file
SYS_PROMPT_PATH = "sys_prompts/system_prompt1.txt"
session = {"configurable": {"session_id": "1"}}

# Load the environment variables
load_dotenv(override=True)

# Initialize the chat History
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


model = ChatOpenAI(model="gpt-3.5-turbo")

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


def calculate_complexity(code_text, output_label):
    """
    Function to calculate the complexity of the given code text
    and update the output label with the response.
    """
    response = llm_with_history.invoke(
                code_text,
                config=session,
            )
    #print(response.content)  # Print the response to the console
    output_label['text'] = response.content  # Update the label in the GUI