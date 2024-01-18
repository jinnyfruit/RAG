from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

huggingface_token = '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'

model_name = "meta-llama/Llama-2-7b-chat-hf"
tokenizer = AutoTokenizer.from_pretrained(model_name, use_auth_token=huggingface_token)
model = AutoModelForCausalLM.from_pretrained(model_name, use_auth_token=huggingface_token)

def generate_text(prompt, max_length=50):
    input_ids = tokenizer.encode(prompt, return_tensors="pt")
    output = model.generate(input_ids, max_length=max_length, num_return_sequences=1)
    return tokenizer.decode(output[0], skip_special_tokens=True)

prompt = "The future of technology is"
generated_text = generate_text(prompt)
print(generated_text)
