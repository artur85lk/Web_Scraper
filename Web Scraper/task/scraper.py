import requests
from bs4 import BeautifulSoup
import re

def link_text(link_end):
    text = ""
    url_article = f"https://www.nature.com{str(link_end)}"
    page_content2 = requests.get(url_article)
    soup2 = BeautifulSoup(page_content2.content, 'html.parser')
    article_text = soup2.find_all('article')
    for p in article_text:
        text += p.text + '\n'
    return text

url = "https://www.nature.com/nature/articles?sort=PubDate&year=2020&page=3"
page_content = requests.get(url)

soup = BeautifulSoup(page_content.content, 'html.parser')
article = soup.find_all('a', {'class':"c-card__link u-link-inherit"})
news = soup.find_all('span', {'class':"c-meta__type"})
x = {}
counter = 0
for k in article:
    x[k] = news[counter].text
    counter += 1
print(x)
for p, news in x.items():
    if news == "News":
        title = p.text
        new_title = ""
        for i in title:
            if bool(re.match('\w', i)) or i == " ":
                new_title += i
        new_title = new_title.replace(" ", "_")
        text_article = str(link_text(p.get('href')))
        with open(f"{new_title}.txt", "wb") as f:
            f.write(text_article.encode())
