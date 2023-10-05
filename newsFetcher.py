import requests
api_key="67848e91644e4e8d9dce4e8bba97f66d"
def get_news_headlines():
    base_url = "https://newsapi.org/v2/"
    params = {
        "apiKey": api_key,
        "country": "us",
        "language": "en",
        "pageSize": 20
    }

    # Fetch technology headlines
    tech_headlines = fetch_headlines(base_url + "top-headlines", params, category="technology")

    # Fetch business headlines
    biz_headlines = fetch_headlines(base_url + "top-headlines", params, category="business")

    # Fetch special headlines
    special_headlines = fetch_special_headlines(base_url + "everything", params)

    # Combine all the headlines into one dictionary
    all_headlines = {
        **tech_headlines,
        **biz_headlines,
        **special_headlines
    }

    return all_headlines


def fetch_headlines(url, params, category):
    params["category"] = category
    response = requests.get(url, params=params)

    if response.status_code != 200:
        print(f"Error: Failed to fetch {category} headlines. Status code: {response.status_code}")
        return {}

    data = response.json()

    if "articles" not in data:
        print(f"Error: 'articles' key not found in {category} headlines response.")
        return {}

    return extract_titles_and_urls(data)


def fetch_special_headlines(url, params):
    params["sources"] = "the-verge,business-insider,fortune"
    response = requests.get(url, params=params)

    if response.status_code != 200:
        print("Error: Failed to fetch special headlines. Status code: {response.status_code}")
        return {}

    data = response.json()

    if "articles" not in data:
        print("Error: 'articles' key not found in special headlines response.")
        return {}

    return extract_titles_and_urls(data)


def extract_titles_and_urls(data):
    url_list = {}
    for article in data.get("articles", []):
        title = article.get("title")
        url = article.get("url")
        if title and url:
            url_list[title] = url
    return url_list


