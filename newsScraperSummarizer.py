from bs4 import BeautifulSoup
import re
import requests
import newsSummaryTagging

# Cleans up repeated articles
def remove_duplicates(articles):
    seen_urls = set()
    unique_articles = []
    
    for article in articles:
        url = article.get("Url")
        if url not in seen_urls:
            seen_urls.add(url)
            unique_articles.append(article)
    
    return unique_articles


def newsScraper(urls):
    articles_list = []
    # Set the user agent
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
    }

    # Parse the JSON object containing titles and URLs
    

    # Send a GET request to each URL with a delay of 1 second between requests
    for key, value in urls.items():
        title = value["title"]
        
        last_hyphen_index = title.rfind('-')
        if last_hyphen_index != -1:
            title = title[:last_hyphen_index].strip()

            
        url = value["url"]
        source_name = value["source_name"]

        if title and url:
            response = requests.get(url, headers=headers)

            # Use BeautifulSoup to parse the HTML content of the response
            soup = BeautifulSoup(response.content, 'html.parser')

            # Find the tags, which are the most relevant, in the HTML content
            paragraphs = ""
            for p in soup.find_all('p'):
                paragraphs = paragraphs + " " + (p.text)
            
            content = re.sub(r'[^\S ]+', ' ', paragraphs).strip()
            summary = newsSummaryTagging.newsSummarizer(content)

            # Create a dictionary for the article
            article_dict = {
                "Title": title,
                "Url": url,
                "Source": source_name,
                "Content": content,
                "Summary": summary
            }

            articles_list.append(article_dict)
            

    return remove_duplicates(articles_list)
