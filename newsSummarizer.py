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

def extract_domain(link):
  """Extracts the domain name from the given link."""

  regex = r'https?://(?:www\.)?([^/]+)\.com'
  match = re.search(regex, link)

  if match:
    return match.group(1)
  else:
    return None
# Function to generate HTML content
def generate_html(articles):
    html_content = """
    <!DOCTYPE html>
    <html>
    <head>
      <title>News Articles</title>
        <meta charset="UTF-8">
        <link rel="stylesheet" href="style.css">
        <link href='https://fonts.googleapis.com/css?family=Roboto' rel='stylesheet'>
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
        author = extract_domain(url)
        content = article["Content"]
        if title != "" and url != "" and content != "":
            summarized_content = summarize_text(content)

            article_html = f"""
            <div class="lefty"><h2><a href="{url}">{title}</a></h2><span class="link">--{author}</span></div>
            
            <div class="righty">
            <p class="summary">{summarized_content}</p>
            <span class="element-title" onclick="toggleExpand(this)">Read</span>
            <p  class="element-article">{content}</p>
            """
            html_content += article_html

    html_content += """
    </body>
    </html>
    """
    
    return html_content


