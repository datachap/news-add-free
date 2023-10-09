import requests
import json

def get_news_headlines():
    api_key="67848e91644e4e8d9dce4e8bba97f66d"
    url_list = {}   
    base_url = "https://newsapi.org/v2/"
    params = {
        "apiKey": api_key,
        "language": "en",
    }

    # Fetch category headlines
    fetch_category_headlines(base_url + "top-headlines", params, category="technology", url_list=url_list)
    fetch_category_headlines(base_url + "top-headlines", params, category="business", url_list=url_list)
    fetch_category_headlines(base_url + "top-headlines", params, category="general", url_list=url_list)

    # Fetch domains headlines
    fetch_domain_headlines("https://newsapi.org/v2/everything?domains=theverge.com,techcrunch.com,www.businessinsider.com/,fortune.com&pageSize=1&apiKey=67848e91644e4e8d9dce4e8bba97f66d", url_list=url_list)

    return url_list


def fetch_category_headlines(url, params, category, url_list):
    params["category"] = category
    params["country"] = "us"
    params["pageSize"] = 1
    response = requests.get(url, params=params)

    if response.status_code != 200:
        print(f"Error: Failed to fetch {category} headlines. Status code: {response.status_code}")
        return {}

    data = response.json()

    if "articles" not in data:
        print(f"Error: 'articles' key not found in {category} headlines response.")
        return {}
    return extract_titles_and_urls(data, url_list)


def fetch_domain_headlines(url,url_list):
   
    response = requests.get(url)

    if response.status_code != 200:
        print("Error: Failed to fetch headlines with domains. Status code: {response.status_code}")
        return {}

    data = response.json()

    if "articles" not in data:
        print("Error: 'articles' key not found in headlines with domains.")
        return {}
    return extract_titles_and_urls(data, url_list)



def extract_titles_and_urls(data, url_list):

    for article in data.get("articles", []):
        title = article.get("title")
        url = article.get("url")
        name = article.get("source", {}).get("name")
        if title and url and "youtube.com" not in url:
            url_list[title] = {"title": title, "url": url, "source_name": name}
    
    return url_list



