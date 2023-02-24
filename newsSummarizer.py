from transformers import PegasusForConditionalGeneration, PegasusTokenizer
import json

def textSummarizerWorker(maxLengthSingleOrNot, summarizedNewsList, text2Summarize, model, tokenizer, title):
    inputs = tokenizer(text2Summarize, padding='max_length', truncation=True, max_length=maxLengthSingleOrNot, return_tensors="pt")
    input_ids = inputs['input_ids']
    attention_mask = inputs['attention_mask']
    n_segments = input_ids.shape[-1] // maxLengthSingleOrNot
    
    summary = ""
    for i in range(n_segments+1):
            start = i * maxLengthSingleOrNot
            end = (i+1) * maxLengthSingleOrNot
            input_ids_segment = input_ids[:, start:end]
            attention_mask_segment = attention_mask[:, start:end]
            if input_ids_segment.numel() == 0 or attention_mask_segment.numel() == 0:
                continue  # skip empty segments
            outputs = model.generate(input_ids_segment, max_length=maxLengthSingleOrNot, early_stopping=True)
            summary_segment = tokenizer.decode(outputs[0], skip_special_tokens=True)
            summary += summary_segment
            
    summarizedNewsList[title] = summary
    

def textSummarizer(scrapedNews, singleOrNotSummary):
    
    # The document where it will be printed, the newsList after summarized and the total summary put together
    file2Print = ""
    summarizedNewsList = {}
    totalSummary = ""
    
    # Check if this the summary of the single links or not
    if singleOrNotSummary:
        maxLengthSingleOrNot = 250
        file2Print = "data.json"
    else:
        maxLengthSingleOrNot= 1000
        file2Print = "data1.json"
    
    # Load the Pegasus model and tokenizer
    model = PegasusForConditionalGeneration.from_pretrained('google/pegasus-large')
    tokenizer = PegasusTokenizer.from_pretrained('google/pegasus-large')

    if isinstance(scrapedNews, dict):
        for title, text2Summarize in scrapedNews.items():
            totalSummary += text2Summarize
            textSummarizerWorker(maxLengthSingleOrNot, summarizedNewsList, text2Summarize, model, tokenizer, title)
    elif isinstance(scrapedNews,str):
        textSummarizerWorker(maxLengthSingleOrNot, summarizedNewsList, scrapedNews, model, tokenizer, "Final")
        
    with open(file2Print, 'w', encoding='utf-8') as f:
        json.dump(summarizedNewsList, f, ensure_ascii=False, indent=4)
    return totalSummary
            
