import pandas as pd
import json
from transformers import AutoTokenizer, AutoModel
import faiss
import numpy as np

# Load the dataset
with open('생활법령.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

# Convert to DataFrame
df = pd.DataFrame(data)
df.columns = ['question', 'answer']

# 벡터화 및 벡터DB 구축
model_name = "jiwoochris/ko-llama2-v1" 
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModel.from_pretrained(model_name)

def encode_questions(questions):
    inputs = tokenizer(questions, padding=True, truncation=True, return_tensors="pt")
    outputs = model(**inputs)
    return outputs.last_hidden_state[:, 0, :].detach().numpy()

question_vectors = encode_questions(df["question"].tolist())

dim = question_vectors.shape[1]
index = faiss.IndexFlatL2(dim)
index.add(question_vectors)

def find_similar_question(query, k=1):
    query_vector = encode_questions([query])
    D, I = index.search(query_vector, k)
    return df.iloc[I[0][0]]

def generate_answer_with_context(context, question):
    input_text = f"질문에 대해서 관련 정보를 참고해서 사실만을 기반으로 답변해줘. 질문: {question} 관련 정보: {context}"
    inputs = tokenizer(input_text, return_tensors="pt")
    output_sequences = model.generate(input_ids=inputs['input_ids'], 
                                      attention_mask=inputs['attention_mask'], 
                                      max_length=512)
    return tokenizer.decode(output_sequences[0], skip_special_tokens=True)

# 모델 로드 후 사용자 입력 처리
while True:
    customer_query = input("질문을 입력하세요 (0을 입력하면 종료됩니다.): ")
    if customer_query == '0':
        break

    similar_question = find_similar_question(customer_query)
    context = similar_question['answer']
    generated_answer = generate_answer_with_context(context, customer_query)

    print("LLM 답변:", generated_answer)
    print("참고한 질문:", similar_question['question'])
    print("참고한 답변:", context)