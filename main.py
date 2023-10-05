import os
import subprocess
from newsFetcher import get_news_headlines
from newsScraper import getNewsInfo
from newsSummarizer import generate_html

def main():
    # Get the news list from the scraper
    headlines = get_news_headlines()
    
    html_content = generate_html(getNewsInfo(headlines))

    # Save the HTML content to a file
    with open("news.html", "w", encoding="utf-8") as html_file:
        html_file.write(html_content)

    # Commit and push changes to GitHub
    commit_and_push_changes()

def commit_and_push_changes():
    # Add news.html to Git staging area
    subprocess.run(["git", "add", "news.html"])
    
    # Commit the changes with a message
    subprocess.run(["git", "commit", "-m", "Update news.html"])

    # Push the changes to GitHub
    subprocess.run(["git", "push"])

if __name__ == "__main__":
    main()
