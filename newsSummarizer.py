from transformers import AutoModelForSeq2SeqLM, BartTokenizer
import os
import json
from newsFetcher import getNewsHeadlinesUrl
from newsScraper import getNewsInfo

def textSummarizer(scrapedNews, singleOrNotSummary):
    
    # Check if this the summary of the single links or not
    if singleOrNotSummary:
        maxLengthSingleOrNot = 100
        if os.path.exists("data.json"):
            os.remove("data.json")
    else:
        maxLengthSingleOrNot= 1000
        if os.path.exists("data1.json"):
            os.remove("data1.json")
            
    summarizedNewsList = {}
    toBeFinallySummarized = {}
    totalSummary = ""
# Load the BART model and tokenizer
    model = AutoModelForSeq2SeqLM.from_pretrained("facebook/bart-large-cnn")
    tokenizer = BartTokenizer.from_pretrained("facebook/bart-large-cnn")
    counter = 0

    for title, text2Summarize in scrapedNews.items():
        print (counter)
        max_length = 512
        inputs = tokenizer(text2Summarize, padding='max_length', truncation=True, max_length=max_length, return_tensors="pt")
        input_ids = inputs['input_ids']
        attention_mask = inputs['attention_mask']
        n_segments = input_ids.shape[-1] // max_length

        # summarize each segment and concatenate the results
        summary = ""
        for i in range(n_segments+1):
            start = i * max_length
            end = (i+1) * max_length
            input_ids_segment = input_ids[:, start:end]
            attention_mask_segment = attention_mask[:, start:end]
            if input_ids_segment.numel() == 0 or attention_mask_segment.numel() == 0:
                continue  # skip empty segments
            outputs = model.generate(input_ids_segment, attention_mask=attention_mask_segment, max_length=maxLengthSingleOrNot, early_stopping=False)
            summary_segment = tokenizer.decode(outputs[0], skip_special_tokens=True)
            summary += summary_segment
            
        totalSummary += summary
        summarizedNewsList[title] = summary
        counter = counter + 1
    toBeFinallySummarized["Final"] = totalSummary
        
        
    if singleOrNotSummary:  
        with open('data.json', 'w', encoding='utf-8') as f:
            json.dump(summarizedNewsList, f, ensure_ascii=False, indent=4)
        return toBeFinallySummarized
    else:
        with open('data1.json', 'w', encoding='utf-8') as f:
            json.dump(toBeFinallySummarized, f, ensure_ascii=False, indent=4)
        