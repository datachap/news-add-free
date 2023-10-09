import json
from newsFetcher import get_news_headlines
from newsScraperSummarizer import newsScraper

def main():
    # Get the news list from the scraper
    headlines = get_news_headlines()
    finalizedNews = newsScraper(headlines)
    with open ("data.json", "w") as f:
        json.dump(finalizedNews, f)

    

if __name__ == "__main__":
    main()
