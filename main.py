import unittest
import requests
from bs4 import BeautifulSoup

def get_news_headlines(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    headlines = soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6'])  # get all headers

    return [headline.get_text() for headline in headlines]

class TestGetNewsHeadlines(unittest.TestCase):

    def setUp(self):
        # URL для тестирования
        self.url = 'https://www.bbc.com/news'
        # Получаем заголовки перед каждым тестом
        self.headlines = get_news_headlines(self.url)

    def test_status_code(self):
        # Проверяем статус код ответа
        response = requests.get(self.url)
        self.assertEqual(response.status_code, 200)

    def test_not_empty_response(self):
        # Проверяем, что ответ не пустой
        self.assertIsNotNone(self.headlines)
        self.assertIsInstance(self.headlines, list)

    def test_min_10_headlines(self):
        # Проверяем, что в ответе есть минимум 10 заголовков
        self.assertGreaterEqual(len(self.headlines), 10)

if __name__ == '__main__':
    unittest.main()
