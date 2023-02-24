from bs4 import BeautifulSoup
import re
import requests
from newsFetcher import getNewsHeadlinesUrl

def getNewsInfo(urls):
    
    # Set the user agent
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}
    contentDictionary = {}
    
    # Send a GET request to the URL with a delay of 1 second between requests
    for title, url in urls.items():
        response = requests.get(url, headers=headers)

        # Use BeautifulSoup to parse the HTML content of the response
        soup = BeautifulSoup(response.content, 'html.parser')

        # Find the tags, which are the most relevant, in the HTML content
        p_paragraphs = ""
        for p in soup.find_all('p'):
            p_paragraphs = p_paragraphs + " " + (p.text)
        
        contentDictionary[title] = re.sub(r'[^\S ]+', ' ', p_paragraphs)
            
    return contentDictionary





