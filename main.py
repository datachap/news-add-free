from newsFetcher import get_news_headlines
from newsScraper import getNewsInfo
from newsSummarizer import generate_html

def main():
    # Get the news list from the scraper
    headlines = get_news_headlines()
    
    html_content = generate_html(getNewsInfo(headlines))

    # Save the HTML content to a file (you can also serve it using a web server)
    with open("news.html", "w", encoding="utf-8") as html_file:
        html_file.write(html_content)

if __name__ == "__main__":
    main()
    