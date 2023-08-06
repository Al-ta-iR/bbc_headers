import unittest
import requests
from bs4 import BeautifulSoup

def get_news_headlines(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise exception for 4xx or 5xx errors
        soup = BeautifulSoup(response.text, 'html.parser')
        headlines = soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6'])  # get all headers
        return [headline.get_text() for headline in headlines]
    except requests.exceptions.MissingSchema:
        print(f"Invalid URL: {url}. No scheme supplied. Perhaps you meant 'https://'?")
        return []
    except requests.exceptions.RequestException as e:
        print(f"Error fetching the URL: {e}")
        return []

class TestGetNewsHeadlines(unittest.TestCase):

    def test_valid_url(self):
        url = 'https://www.bbc.com/news'
        headlines = get_news_headlines(url)
        self.assertIsNotNone(headlines)
        self.assertIsInstance(headlines, list)
        self.assertGreater(len(headlines), 0)

    def test_invalid_url(self):
        url = 'https://www.invalidurl.com'
        headlines = get_news_headlines(url)
        self.assertEqual(headlines, [])

    def test_empty_url(self):
        url = ''
        headlines = get_news_headlines(url)
        self.assertEqual(headlines, [])

if __name__ == '__main__':
    unittest.main()
