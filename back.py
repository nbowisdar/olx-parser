url = 'https://www.olx.ua/hobbi-otdyh-i-sport/antikvariat-kollektsii/dnp/q-монеты/'
import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
agent = UserAgent().random
headers = {
    "Accept": "*/*",
    "User-Agent": agent
}
s = requests.get(url, headers)
data = {}
soup = BeautifulSoup(s.text,'lxml')

info = soup.find(class_='fixed offers breakword redesigned').find_all(class_='lheight22 margintop5')
links = [i.find('a').get('href') for i in info]
prices = [i.text.replace('\n','') for i in soup.find(class_='fixed offers breakword redesigned').find_all('div',class_='space inlblk rel')]
for i in range(len(prices)):
    data[links[i]] = prices[i]
'TEST'

