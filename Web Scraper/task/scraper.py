import requests
from bs4 import BeautifulSoup

print("Input the URL:")
# https://web.archive.org/web/20220310110507/https://www.imdb.com/title/tt0080684/

url = input()
movie = {}
r = requests.get(url, headers={'Accept-Language': 'en-US,en;q=0.5'})
soup = BeautifulSoup(r.content, 'html.parser')

try:
    paragraphs = soup.find('h1')
    movie["title"] = paragraphs.text

    description1 = soup.find_all('span',{'data-testid': 'plot-l'})

    for i in description1:
        movie["description"] = i.text
    if movie["title"] != "" and movie["description"] != "":
        print(movie)
    else:
        print("Invalid quote resource!")
except Exception:
    print()
    print("Invalid movie page!")
