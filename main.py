from turtle import title
import requests
from bs4 import BeautifulSoup
from newspaper import Article
import pandas as pd
from tqdm import tqdm

def scrapAll():
    page = 2
    scraptedData = []
    while True:

        page_url = f'https://www.indiegamewebsite.com/category/reviews/page/{page}/'

        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
        result = requests.get(page_url, headers=headers)
        html = result.content.decode()
        soap = BeautifulSoup(html, 'lxml')
        links = soap.findAll("div", {"class": "article--thumb__title"})
        page += 1
        for link in tqdm(links):
            news_url = link.a['href']
            try:
                article = Article(news_url)
                article.download()
                article.parse()
            except:
                print('error')
            scraptedData.append({
                'url': news_url,
                'text': article.text,
                'title': article.title
            })
        if page == 3:
            break

    df = pd.DataFrame(scraptedData)
    df.to_csv(f'IndieGames.csv')
    print(scraptedData)


scrapAll()