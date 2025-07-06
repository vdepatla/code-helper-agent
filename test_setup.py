import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

# Load environment variables from .env file
load_dotenv()   

# Get the OpenAI API key from environment variables
openai_api_key = os.getenv("OPENAI_API_KEY")    
if not openai_api_key:
    raise ValueError("OPENAI_API_KEY is not set in the environment variables.")

# Initialize the OpenAI chat model
llm = ChatOpenAI(model="gpt-4o")

# Test the model with a simple prompt
response = llm.invoke("Tell me some cool things about san diego?")
print(response)