from langchain.chains import LLMChain
from langchain_openai import OpenAI
from langchain.prompts import PromptTemplate
from langchain.utilities.dalle_image_generator import DallEAPIWrapper

import os
from dotenv import load_dotenv

load_dotenv()

# 환경 변수를 통해 OpenAI API 키를 설정합니다.
os.environ["OPENAI_API_KEY"] = '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'

# OpenAI 클래스를 인스턴스화합니다.
llm = OpenAI(temperature=0.9)

prompt = PromptTemplate(
    input_variables=["image_desc"],
    template="Generate a prompt to generate an image based on the following description: {image_desc}",
)
chain = LLMChain(llm=llm, prompt=prompt)

image_prompt = chain.run("Red apple")
print(image_prompt)

# DallEAPIWrapper 인스턴스를 생성합니다.
dalle_api_wrapper = DallEAPIWrapper()
image_url = dalle_api_wrapper.run(image_prompt)
print(image_url)
