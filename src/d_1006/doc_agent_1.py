from dotenv import load_dotenv
from langchain.agents import create_agent

load_dotenv()

def get_weather(city: str) -> str:
    """Get weather for a given city."""
    return f"It's always sunny in {city}!"

agent = create_agent(
    model="openai:gpt-5.5",
    tools=[get_weather],
    system_prompt="You are a helpful assistant.",
)

result = agent.invoke(
    {"messages": [{"role": "user", "content": "세종 날씨는 어때?"}]}
)

print(result["messages"][-1].content_blocks)


# cmd -1
# (agent) D:\hykim\agent\src\d_1006>uv run python -m doc_agent_1.py

# [{'type': 'text', 'text': '세종은 현재 맑은 날씨입니다. ☀️'}]

# D:\hykim\agent\.venv\Scripts\python.exe: 
# Error while finding module specification for 'doc_agent_1.py' 
# (ModuleNotFoundError: __path__ attribute not found on 'doc_agent_1' while trying to find 'doc_agent_1.py'). 
# Try using 'doc_agent_1' instead of 'doc_agent_1.py' as the module name.



# cmd -2
# (agent) D:\hykim\agent\src\d_1006>uv run python -m doc_agent_1   

# [{'type': 'text', 'text': '세종 날씨는 맑습니다. ☀️'}]



print(result["messages"][-1].content)



# cmd -3
# (agent) D:\hykim\agent\src\d_1006>uv run python -m doc_agent_1
# 세종은 현재 맑은 날씨예요. ☀️
