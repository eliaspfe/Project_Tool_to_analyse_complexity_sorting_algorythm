import getpass
from dotenv import load_dotenv
import os
from langchain_openai import ChatOpenAI

os.environ["OPENAI_API_KEY"] = "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"

model = ChatOpenAI(model="gpt-3.5-turbo")

from langchain_core.messages import HumanMessage

response = model.invoke([HumanMessage(content="Hi! I'm Bob")])
print(response)