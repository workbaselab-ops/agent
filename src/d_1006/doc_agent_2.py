from dotenv import load_dotenv
from pydantic import BaseModel
from langchain.agents import create_agent
from langchain.tools import tool

load_dotenv()

class Answer(BaseModel):
    summary : str
    confidence : float

@tool
def search(query: str) -> str:
    """Search for information."""
    return f"Results for: {query}"

agent = create_agent(
    model="openai:gpt-5.5",
    tools=[search],
    response_format=Answer,
    system_prompt="너는 학습 도우미야, 핵심과 간단구조를 알려줘.",
)

result = agent.invoke(
    {"messages": [{"role": "user", "content": "싱글 에이전트를 설명해줘"}]}
    )

print(result["structured_response"])



# summary='싱글 에이전트(Single Agent)는 하나의 에이전트가 목표를 달성하기 위해 환경을 관찰하고, 판단하고, 행동하는 구조를 말해요.\n\n
# 
# 핵심 구조:\n
# 1. 목표: 에이전트가 달성해야 할 일\n
# 2. 관찰: 현재 상황이나 데이터를 확인\n
# 3. 판단: 무엇을 할지 결정\n
# 4. 행동: 선택한 행동을 실행\n
# 5. 결과 확인: 행동 후 변화된 상태를 다시 관찰\n\n
# 
# 예시:\n
# - 청소 로봇 1대가 방을 돌아다니며 먼지를 찾고 청소하는 경우\n
# - 챗봇 하나가 사용자의 질문을 이해하고 답변하는 경우\n
# - 게임 캐릭터 하나가 적을 피하거나 공격하는 경우\n\n
# 
# 특징:\n
# - 에이전트가 1개뿐이라 구조가 단순함\n
# - 다른 에이전트와 협력하거나 경쟁하지 않음\n
# - 의사결정이 비교적 명확함\n\n
# 
# 비교:\n
# - 싱글 에이전트: 혼자 판단하고 행동함\n
# - 멀티 에이전트: 여러 에이전트가 서로 협력하거나 경쟁함\n\n
# 
# 한 줄 정리: 싱글 에이전트는 하나의 주체가 환경을 보고 스스로 판단해 행동하는 시스템입니다.' confidence=0.99