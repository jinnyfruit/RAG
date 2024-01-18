from langchain.agents.agent_types import AgentType
from langchain.chat_models import ChatOpenAI
from langchain_experimental.agents.agent_toolkits import create_pandas_dataframe_agent
import pandas as pd

# dotenv 라이브러리를 사용하여 환경 변수 로드
from dotenv import load_dotenv
load_dotenv()

# pandas를 사용하여 Excel 파일 로드
df = pd.read_excel("HR_Management_Dummy_File.xlsx")

# api_key.txt 파일에서 API 키 읽기
with open('api_key.txt', 'r') as file:
    openai_api_key = file.read().strip()

# ChatOpenAI 인스턴스 생성, API 키를 매개변수로 전달
agent = create_pandas_dataframe_agent(
    ChatOpenAI(temperature=0, model="gpt-3.5-turbo-0613", openai_api_key=openai_api_key),
    df,
    verbose=True,
    agent_type=AgentType.OPENAI_FUNCTIONS,
)

# 에이전트 실행
agent.run("연봉 5000만원 넘는 사람이 누구야?")