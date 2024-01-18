from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

# Load the tokenizer and model
tokenizer = AutoTokenizer.from_pretrained("EleutherAI/polyglot-ko-1.3b")
model = AutoModelForCausalLM.from_pretrained("EleutherAI/polyglot-ko-1.3b")

# Your prompt text in Korean
prompt_text = "한국의 전통 문화에 대해 설명해 주세요."

# Encode the prompt text
inputs = tokenizer(prompt_text, return_tensors='pt')

# Generate a response considering the attention mask
output_sequences = model.generate(
    input_ids=inputs['input_ids'],
    attention_mask=inputs['attention_mask'],
    max_length=100,
    num_return_sequences=1,
    no_repeat_ngram_size=2,
    #temperature=0.7,
    pad_token_id=tokenizer.eos_token_id
)

# Decode the generated text
generated_text = tokenizer.decode(output_sequences[0], skip_special_tokens=True)

print(generated_text)
