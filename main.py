import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import json
import re

# agent = UserAgent().random
# headers = {
#     "Accept": "*/*",
#     "User-Agent": agent
# }

# link = 'https://www.olx.ua/hobbi-otdyh-i-sport/antikvariat-kollektsii/dnp/q-монеты/'
# link2 = 'https://loot.farm/ru/'
# link3 = 'https://www.google.com/'
# page = requests.get(link, headers)
#
# with open('file.txt', 'w') as file:
#     file.write(page.text)
#     print(file)

with open('file.txt') as file:
    f = file.read()
soup = BeautifulSoup(f, 'lxml')

data = soup.find_all(class_='lheight22 margintop5')

info_link = [str(re.findall('href=".+"', f'''{data[0]}'''))[8:-3] for i in data]
info_name = [i.text.strip() for i in data]

for i in range(len(info_name)):
    print(info_name[i] + ' Ссылка: '+ info_link[i])



