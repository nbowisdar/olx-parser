import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
agent = UserAgent().random
headers = {
    "Accept": "*/*",
    "User-Agent": agent
}
data = {}
def show_last(url):
    s = requests.get(url, headers).text
    soup = BeautifulSoup(s, 'lxml')
    link = soup.find(class_='fixed offers breakword redesigned').find(class_='lheight22 margintop5').find('a').get('href')
    if link not in data:
        price = soup.find(class_='fixed offers breakword redesigned').find('div',class_='space inlblk rel').text.replace('\n', '').strip()
        data[link] = price
        return f'{link}, {price}'
    return(False)


def show_all(url):
    s = requests.get(url, headers)
    soup = BeautifulSoup(s.text,'lxml')
    info = soup.find(class_='fixed offers breakword redesigned').find_all(class_='lheight22 margintop5')
    links = [i.find('a').get('href') for i in info]
    prices = [i.text.replace('\n','') for i in soup.find(class_='fixed offers breakword redesigned').find_all('div',class_='space inlblk rel')]
    for i in range(len(prices)):
        data[links[i]] = prices[i]



#print(show_last('https://www.olx.ua/dnp/q-айфон-7/'))
