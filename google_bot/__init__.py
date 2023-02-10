import requests
from bs4 import BeautifulSoup
from datetime import datetime

class bot_google():
    def __init__(self,keyword="deprem bağış yap"):

        now = datetime.now()
        slug = f'{now.strftime("%Y%m%d%H%M%S")}'
        url = f'https://www.google.com/search?q={keyword}'
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
        response = requests.get(url, headers=headers)
        html = response.text

        soup = BeautifulSoup(html, 'html.parser')
        results = soup.find_all('div', class_='g')

        for result in results:
            link = result.find('a').get('href')
            result = f'{link}'
            self.write_result(result)

    def write_result(self,link):
        print(link)
