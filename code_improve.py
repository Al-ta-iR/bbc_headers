import requests 
from bs4 import BeautifulSoup

def get_news_headlines():
    soup = BeautifulSoup(requests.get('https://www.bbc.com/news').text, 'html.parser')
    return [h.text for h in soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6'])]

print(get_news_headlines())