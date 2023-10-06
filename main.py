import os
import subprocess
from newsFetcher import get_news_headlines
from newsScraper import getNewsInfo
from newsSummarizer import generate_html

def main():
    # Get the news list from the scraper
    headlines = get_news_headlines()
    print("Total number of articles: " + str(len(headlines)))
    
    html_content = generate_html(getNewsInfo(headlines))

    # Save the HTML content to a file
    with open("index.html", "w", encoding="utf-8") as html_file:
        html_file.write(html_content)


if __name__ == "__main__":
    main()
