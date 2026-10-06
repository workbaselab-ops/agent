from dotenv import load_dotenv
from pydantic import BaseModel
from langchain.agents import create_agent
from langchain.tools import tool

load_dotenv()

calss Answer(BaseModel):

