from bs4 import BeautifulSoup
from transformers import AutoModelForSeq2SeqLM, BartTokenizer
import re
import requests
from transformers import PegasusForConditionalGeneration, PegasusTokenizer

# Define the Pegasus model and tokenizer
model = AutoModelForSeq2SeqLM.from_pretrained("facebook/bart-large-cnn")
tokenizer = BartTokenizer.from_pretrained("facebook/bart-large-cnn")

# Function to summarize the content
def summarize_text(text):
    max_length = 350  # Increase max_length for longer summaries
    inputs = tokenizer.encode("summarize: " + text, max_length=1024, return_tensors="pt", truncation=True)
    summary_ids = model.generate(inputs, max_length=max_length, min_length=150, length_penalty=2.0, num_beams=4, early_stopping=True)
    summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
    return summary

# Function to generate HTML content
def generate_html(articles):
    html_content = """
    <!DOCTYPE html>
    <html>
    <head>
    <meta charset="UTF-8">
        <title>News Articles</title>
               <style>
        body {
            font-family: Arial, sans-serif;
        }

        h1 {
            color: #336699;
        }

        h2 {
            color: #444;
        }

        .element {
            font-weight: bold;
            color: #888;
        }

        .element-article {
            display: none;
            margin-top: 10px;
        }

        .element-article.expanded {
            display: block;
        }

        a {
            text-decoration: none;
            color: #0078d4;
        }

        a:hover {
            text-decoration: underline;
        }
    </style>
    <script>
        // JavaScript to toggle the 'expanded' class on click
        function toggleExpand(element) {
            var articleElement = element.nextElementSibling;
            articleElement.classList.toggle("expanded");
        }
    </script>
        
    </head>
    <body>
    """

    # Count the total number of articles
    total_articles = len(articles)
    
    # Modify the <h1> tag to include the total number of articles
    html_content += f"<h1> News ({total_articles} articles)</h1>"
    i = 0
    for article in articles:
        i = i + 1
        print (i)
        title = article["Title"]
        url = article["Url"]
        content = article["Content"]
        if title != "" and url != "" and content != "":
            summarized_content = summarize_text(content)

            article_html = f"""
            <h2><a href="{url}">{title}</a></h2>
            <p class="element">Summary </p>
            <p>{summarized_content}</p>
            <h2 class="element-title" onclick="toggleExpand(this)">Article </h2>
            <p  class="element-article">{content}</p>
            <hr>
            """
            html_content += article_html

        html_content += """
        </body>
        </html>
        """
    
    return html_content


