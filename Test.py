import getpass
from dotenv import load_dotenv
import os
from langchain_openai import ChatOpenAI


model = ChatOpenAI(model="gpt-3.5-turbo")

from langchain_core.messages import HumanMessage

response = model.invoke([HumanMessage(content="Hi! I'm Bob")])
print(response)