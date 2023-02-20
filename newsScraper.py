from bs4 import BeautifulSoup
import time
import requests
from newsFetcher import getNewsHeadlinesUrl

def getNewsInfo(urls):

    # Set the user agent
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}
    contentDictionary = {}
    # Send a GET request to the URL with a delay of 1 second between requests
    for url in urls:
        response = requests.get(url, headers=headers)

    # Use BeautifulSoup to parse the HTML content of the response
        soup = BeautifulSoup(response.content, 'html.parser')

        # Find the tags, which are the most relevant, in the HTML content
        p_paragraphs = []
        for p in soup.find_all('p'):
            p_paragraphs.append(p.text)
        if soup.h1 is not None:
            contentDictionary[soup.h1.text] = p_paragraphs
        if soup.title is not None:
            contentDictionary[soup.title.text] = p_paragraphs
    return contentDictionary

# This shall be used in the main file
# TODO get the title straight from the json file without needing to do it again.
urls = getNewsHeadlinesUrl()
print (getNewsInfo(urls))


print ("Test")





