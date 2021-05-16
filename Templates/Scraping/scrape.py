import requests
from bs4 import BeautifulSoup

res = requests.get('https://news.ycombinator.com/news')
# print(res.text)
soup = BeautifulSoup(res.text, 'html.parser')
# print(soup.body.contents)
# print(soup.find_all('div'))
# print(soup.find_all('a'))
# print(soup.find('a')) # Find first <a>
# print(soup.a) # Find first <a>
links = soup.select('.storylink')
votes = soup.select('.score')
# print(votes[0])
# print(votes[0].get('id'))

def create_custom_hn(links, votes):
    hn = []
    for idx, item in enumerate(links):
        title = links[idx].getText()
        hn.append(title)
    return hn
print(create_custom_hn(links, votes))