from bs4 import BeautifulSoup
import time
import requests

# URL of the website to extract text from
url = 'https://fortune.com/2023/02/17/bao-fan-missing-china-renaissance-shares/'

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

# Find the first <p> tag in the HTML content
p_title = soup.find("h1")
p_paragraphs = soup.find('p')
# Get all the text content from the <p> tag
p_text = p_title.get_text() + p_paragraphs.get_text()

# Print the text content
print(p_text)