import requests
from bs4 import BeautifulSoup
import re
import os


def link_text(link_end):
    text = ""
    url_article = f"https://www.nature.com{str(link_end)}"
    page_content2 = requests.get(url_article)
    soup2 = BeautifulSoup(page_content2.content, 'html.parser')
    text = soup2.find("div", {"class": "c-article-body main-content"}).text.strip()
    return text

how_many_websize = int(input()) + 1
name_article = input()

for i in range(1, how_many_websize):
    os.mkdir(f'Page_{i}')

for i  in range(1, how_many_websize):
    url = f"https://www.nature.com/nature/articles?sort=PubDate&year=2020&page={str(i)}"
    page_content = requests.get(url)

    soup = BeautifulSoup(page_content.content, 'html.parser')
    article = soup.find_all('a', {'class':"c-card__link u-link-inherit"})
    news = soup.find_all('span', {'class':"c-meta__type"})
    x = {}
    counter = 0
    for k in article:
        x[k] = news[counter].text
        counter += 1

    for p, news in x.items():

        if news == name_article:
            os.chdir(f'Page_{i}')
            title = p.text
            new_title = ""
            for i in title:
                if bool(re.match('\w', i)) or i == " ":
                    new_title += i
            new_title = new_title.replace(" ", "_")
            text_article = str(link_text(p.get('href')))
            print(text_article)
            with open(f"{new_title}.txt", "wb") as f:
                f.write(text_article.encode())
