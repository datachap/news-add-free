from transformers import AutoModelForSeq2SeqLM, BartTokenizer, BartForConditionalGeneration
import torch

model = AutoModelForSeq2SeqLM.from_pretrained("facebook/bart-large-cnn")
tokenizer = BartTokenizer.from_pretrained("facebook/bart-large-cnn")
max_length = 350


# Function to summarize the content
def newsSummarizer(text):


    inputs = tokenizer.encode("summarize: " + text, max_length=1024, return_tensors="pt", truncation=True)
    summary_ids = model.generate(inputs, max_length=max_length, min_length=150, length_penalty=2.0, num_beams=4, early_stopping=True)
    summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
    return summary



