import requests
from bs4 import BeautifulSoup

url = "https://news.google.com/rss/search?q=UFO"
response = requests.get(url)
soup = BeautifulSoup(response.content, 'xml')

with open('ufo_news.txt', 'w', encoding='utf-8') as file:
    for item in soup.find_all('item'):
        title = item.title.text if item.title else 'No Title'
        link = item.link.text if item.link else 'No Link'
        source = item.source.text if item.source else 'No Source'
        pub_date = item.pubDate.text if item.pubDate else 'No Date'

        file.write(
            f"Title: {title}\nLink: {link}\nSource: {source}\nDate: {pub_date}\n\n")

print("News items have been written to ufo_news.txt")
