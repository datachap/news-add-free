import json
from newsFetcher import get_news_headlines
from newsScraperSummarizer import newsScraper
from htmlGenerator import generate_html_from_json

def main():
    # Get the news list from the scraper
    headlines = get_news_headlines()
    finalizedNews = newsScraper(headlines)
    with open ("data.json", "w") as f:
        json.dump(finalizedNews, f)
    
    # Example usage: Provide the path to your data.json file
    data_json_file = 'data.json'
    html_code = generate_html_from_json(data_json_file)

    # Write the HTML code to a file
    with open("index.html", "w", encoding='utf-8') as file:
        file.write(html_code)
    

if __name__ == "__main__":
    main()
