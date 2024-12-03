from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.chat_history import (
    BaseChatMessageHistory,
    InMemoryChatMessageHistory,
)
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_community.callbacks import get_openai_callback

# Load the environment variables
load_dotenv(override=True)

#System Prompt Path & additional Prompt Paths
SYS_PROMPT_PATH = "sys_prompts/system_prompt1.txt"
TEST_PROMPT_PATH = "sys_prompts/test_procedure_prompt.txt"


#Array of Algorithm Paths
ALGORITHM_PATHS = {"example_algorithms/bubble_sort.txt", "example_algorithms/insertion_sort.txt", "example_algorithms/quick_sort.txt", "example_algorithms/merge_sort.txt", "example_algorithms/selection_sort.txt", "example_algorithms/binary_search.txt", "example_algorithms/linear_search.txt", "example_algorithms/GCD.txt", "example_algorithms/pythagorean_quadruples.txt"}
algorithms = []
summarized_responses = []

#function to read the content of a file
def read_file(file_path):
    """
    Function to read the content of a file.

    Args:
        file_path (str): The path to the file.

    Returns:
        str: The content of the file.
    """
    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()

# * Initialize the LLM with all necessary components
session = {"configurable": {"session_id": "1"}}
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


model = ChatOpenAI(model="gpt-4o")

# Read System Prompt from File and remove special characters
system_prompt = read_file(SYS_PROMPT_PATH)

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

# Read all the algorithm files
for path in ALGORITHM_PATHS:
    algorithms.append(read_file(path))




#! Step1: Determine the coomplexity for each algorithm
counter = 1
for algorithm in algorithms:
    
    print("Current Algorithm: ", counter)
    llm_with_history.invoke(
        algorithm,
        config=session,
        )
    print("-----------------")
    counter = counter + 1


#! Step2: Invoke LLM to summarize the complexity of the algorithm
input_text = read_file(TEST_PROMPT_PATH)
response = llm_with_history.invoke(
    input_text,
    config=session,
    )
summarized_responses = response.content.split("+++")


#! Step3: Solutions for the algorithms
solution = read_file("solutions_for_testing.txt")
solution_splitted = solution.split("+")

for i in range(len(summarized_responses)):
    print(summarized_responses[i])
    print(solution_splitted[i])
    print("-----------------")