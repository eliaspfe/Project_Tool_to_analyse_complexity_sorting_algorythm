
import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI


model = ChatOpenAI(model="gpt-3.5-turbo")

def calculate_complexity(code_text, output_label):
    """
    Function to calculate the complexity of the given code text
    and update the output label with the response.
    """
    response = model.invoke(code_text)
    #print(response.content)  # Print the response to the console
    output_label['text'] = response.content  # Update the label in the GUI