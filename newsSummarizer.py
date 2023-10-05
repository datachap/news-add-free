from bs4 import BeautifulSoup
import re
import requests
from transformers import PegasusForConditionalGeneration, PegasusTokenizer

# Define the Pegasus model and tokenizer
model_name = "google/pegasus-xsum"
tokenizer = PegasusTokenizer.from_pretrained(model_name)
model = PegasusForConditionalGeneration.from_pretrained(model_name)

# Function to summarize the content
def summarize_text(text, max_length=50):
    # Split the input text into chunks of manageable size
    max_chunk_length = 512  # You can adjust this value as needed
    text_chunks = [text[i:i + max_chunk_length] for i in range(0, len(text), max_chunk_length)]
    
    summaries = []

    for chunk in text_chunks:
        inputs = tokenizer.encode("summarize: " + chunk, return_tensors="pt", max_length=1024, truncation=True)
        summary_ids = model.generate(inputs, max_length=max_length, min_length=50, length_penalty=2.0, num_beams=4, early_stopping=True)
        summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
        summaries.append(summary)

    return " ".join(summaries)

# Function to generate HTML content
def generate_html(articles):
    html_content = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>News Articles</title>
        
    </head>
    <body>
    <h1> News everybody </h1>
    """
    
    for article in articles:
        title = article["Title"]
        url = article["Url"]
        content = article["Content"]
        if title != "" and url != "" and content != "":
            summarized_content = summarize_text(content)

            article_html = f"""
            <h2><a href="{url}">{title}</a></h2>
            <p class="element">Summary </p>
            <p>{summarized_content}</p>
            <p class="element">Article </p>
            <p>{content}</p>
            <hr>
            """
            html_content += article_html

        html_content += """
        </body>
        </html>
        """
    
    return html_content


