# Using the News API to fetch news headlines
import requests

# Defining the method to delive the headlines
def getNewsHeadlinesUrl():
    api_key = "67848e91644e4e8d9dce4e8bba97f66d"
    url = "https://newsapi.org/v2/top-headlines"
    params = {
        "apiKey": api_key,
        "category": "general",
        "language": "en",
        "pageSize": 50
    }

    # make the API request
    response = requests.get(url, params=params)

    # parse the JSON response
    urlList = []
    data = response.json()

    # extract the article titles
    for article in data["articles"]:
        urlList.append(article["url"])
    return urlList
