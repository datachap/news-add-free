from bs4 import BeautifulSoup
import time
import requests
from news_fetcher import getNewsHeadlinesUrl

# URL of the website to extract text from
url = getNewsHeadlinesUrl()

# Set the user agent
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}

# Send a GET request to the URL with a delay of 1 second between requests
while True:
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        break
    time.sleep(1)

# Use BeautifulSoup to parse the HTML content of the response
soup = BeautifulSoup(response.content, 'html.parser')

# Find the tags, which are the most relevant, in the HTML content
p_h1 = soup.find("h1")
p_title = soup.find("title")
p_paragraphs = soup.find('p')

# Get all the text content from the <p> tag
if p_h1 is p_title:
    p_text = p_title.get_text() + p_paragraphs.get_text()
elif p_h1 is not p_title and p_h1 is not None and p_title is not None:
    p_text = p_h1.get_text() + p_title.get_text() + p_paragraphs.get_text()

# Print the text content
print(p_text)

