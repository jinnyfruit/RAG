import pandas as pd
import json
from transformers import AutoTokenizer, AutoModel
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import faiss
import numpy as np

# Load the dataset
with open('생활법령.json', 'r', encoding='utf-8') as file:
    data = json.load(file)
    #print(data)

# Convert to DataFrame
df = pd.DataFrame(data)
#print(df.head())

# Rename columns to 'question' and 'answer' if necessary
df.columns = ['question', 'answer']
print(df.head())

# 벡터화 및 벡터DB 구축 
# 모델과 토크나이저 로드
model_name = "psymon/KoLlama2-7b"  # 예시 모델명
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModel.from_pretrained(model_name)

# 질문 데이터 벡터화
def encode_questions(questions):
    inputs = tokenizer(questions, padding=True, truncation=True, return_tensors="pt")
    outputs = model(**inputs)
    return outputs.last_hidden_state[:, 0, :].detach().numpy()

question_vectors = encode_questions(df["question"].tolist())

# 벡터 데이터베이스 구축
dim = question_vectors.shape[1]
index = faiss.IndexFlatL2(dim)
index.add(question_vectors)

def generate_answer(context, question):
    input_text = f"context: {context} question: {question}"
    inputs = tokenizer(input_text, return_tensors="pt")
    output_sequences = model.generate(input_ids=inputs['input_ids'], 
                                      attention_mask=inputs['attention_mask'], 
                                      max_length=512)

    return tokenizer.decode(output_sequences[0], skip_special_tokens=True)

# Example usage
context = "너는 친절한 법률자문챗봇이야."  # Context information
question = "범법행위를 하고 공소시효가 지나면 죄가 없어지나요?"
answer = generate_answer(context, question)
print("Generated Answer:", answer)

