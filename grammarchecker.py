from transformers import T5ForConditionalGeneration, T5Tokenizer
import torch
 
print(torch.cuda.is_available())
print(torch.__version__)  
 
 
model_name = "samadpls/t5-base-grammar-checker"
tokenizer = T5Tokenizer.from_pretrained(model_name)
model = T5ForConditionalGeneration.from_pretrained(model_name)
 

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)
 

example ="grammar: The man is bite by the dog"     #"grammar: she has eat apples"                #"grammar: The ball is being throwning by her"    #"grammar: This sentences, has bads grammar and spelling!"
 

inputs = tokenizer(example, return_tensors="pt", padding=True, truncation=True).to(device)
 
outputs = model.generate(inputs.input_ids, num_beams=4, num_return_sequences=1, max_length=256, early_stopping=True)
 
corrected_sentence = tokenizer.decode(outputs[0], skip_special_tokens=True)
 
print("Original Sentence:", example)
print("Corrected Sentence:", corrected_sentence)