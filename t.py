from transformers import AutoTokenizer, AutoModelForCausalLM

model_name = "beomi/kollama-13b"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

def generate_answer(question):
    inputs = tokenizer(question, return_tensors="pt")
    output_sequences = model.generate(input_ids=inputs['input_ids'], max_length=50)
    return tokenizer.decode(output_sequences[0], skip_special_tokens=True)

# 예시 사용
question = "서울에서 부산까지 가는 가장 빠른 방법은 무엇인가요?"
answer = generate_answer(question)
print(answer)
