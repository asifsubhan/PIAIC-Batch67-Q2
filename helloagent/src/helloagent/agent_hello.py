#This code defines and runs an AI assistant (agent) 
#Loads environment variables from a .env file using python-dotenv
import os
from dotenv import load_dotenv

#Imports from a  agents Module
from agents import (
    Agent,
    Runner,
    set_default_openai_client,
    AsyncOpenAI,
    OpenAIChatCompletionsModel,
    set_tracing_disabled,
)
#Load Gemini API Key
load_dotenv()
gemini_api_key = os.getenv("GEMINI_API_KEY")
if not gemini_api_key:
    raise ValueError("GEMINI_API_KEY is not set in the environment variables.")
#Configure External Client
external_client = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)
#Set Global Client and Disable Tracing
set_default_openai_client(external_client)
set_tracing_disabled(True)
# Model Setup
model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    openai_client=external_client,
)

#Define and Run the Agent by defining the my_first_agent function and sending the prompt and running it synchrounously and print the result on the console
def my_first_agent():
    agent = Agent(
        name="Assistant",
        instructions="A helpful assistant that can answer questions and provide information.",
        model=model,
    )
    result = Runner.run_sync(agent, "what is the capital of Pakistan?")
    print("\n")
    print(result.final_output)
    print("\n")