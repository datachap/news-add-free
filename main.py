from newsFetcher import getNewsHeadlinesUrl
from newsScraper import getNewsInfo
from newsSummarizer import textSummarizer

def main():
    # Get the news list from the scraper
    urls = getNewsInfo(getNewsHeadlinesUrl())
    print ("Number of articles to be scraped: " + (str)(len(urls)))
    finalText = textSummarizer(urls, True)
    
if __name__ == "__main__":
    main()
    