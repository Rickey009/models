from transformers import AutoModelForCausalLM, AutoTokenizer

access_token = "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"
model_name = "Qwen/Qwen2.5-Coder-32B-Instruct"

model = AutoModelForCausalLM.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)

dir_name = './qwen2'
tokenizer.save_pretrained(dir_name)
model.save_pretrained(dir_name)