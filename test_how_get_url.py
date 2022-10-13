# Тут я экспериментирую, как можно
# получить ссылку на следующую страницу
# К итоговому коду домашки отношение не имеет.


import pprint
import re
from datetime import datetime
from csv import DictWriter

from bs4 import BeautifulSoup
from requests import get


# # flask - всего 19 страниц в результатах поиска
# # FastAPI - всего 2 страницы в результатах поиска
new = f'/feed/?q=flask&page=3'
res = get(f'https://pythondigest.ru{new}')
soup = BeautifulSoup(res.text, 'html.parser')
ss = soup.find('ul', class_='pagination pagination-sm')
# print(ss.prettify())
p = ss.find_all('li')[-1]
print('ss:', ss)
# Вывод:
#    ss: <ul class="pagination pagination-sm"><li><a href="/feed/?q=flask&amp;page=2">←</a></li><li><a href="/feed/?q=flask&amp;page=1">1</a></li><li><a href="/feed/?q=flask&amp;page=2">2</a></li><li class="active"><a>3</a></li><li><a href="/feed/?q=flask&amp;page=4">4</a></li><li><a href="/feed/?q=flask&amp;page=5">5</a></li><li><a href="/feed/?q=flask&amp;page=6">6</a></li><li><a href="/feed/?q=flask&amp;page=7">7</a></li><li><a href="/feed/?q=flask&amp;page=8">8</a></li><li><a href="/feed/?q=flask&amp;page=9">9</a></li><li><a href="/feed/?q=flask&amp;page=10">10</a></li><li></li><li class="disabled"><a>...</a></li><li><a href="/feed/?q=flask&amp;page=18">18</a></li><li><a href="/feed/?q=flask&amp;page=19">19</a></li><li><a href="/feed/?q=flask&amp;page=4">→</a></li></ul>
print('ss.li:', ss.li)
# Вывод:
#    ss.li: <li><a href="/feed/?q=flask&amp;page=2">←</a></li>
print('ss.a:', ss.a)
# Вывод:
#    ss.a: <a href="/feed/?q=flask&amp;page=2">←</a>
print('p:', p)
# Вывод:
#    p: <li><a href="/feed/?q=flask&amp;page=4">→</a></li>
print('p.li:', p.li)
# Вывод:
#    p.li: None
print('p.a:', p.a)
# Вывод:
#    p.a: <a href="/feed/?q=flask&amp;page=4">→</a>
new = p.a.get('href')
print('new:', new)
# Вывод:new: /feed/?q=flask&page=4
#
# while new:
#     res = get(f'https://pythondigest.ru{new}')
#     soup = BeautifulSoup(res.text, 'html.parser')
#     ss = soup.find('ul', class_='pagination pagination-sm')
#     pprint.pprint(ss)
#     p = ss.find_all('li')[-1]
#     print('p:', p)
#     # print(p)
#     new = p.a.get('href')
#     print('new:', new)
#     # print(new)
