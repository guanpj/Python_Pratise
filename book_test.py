import requests
# 引用requests库
from bs4 import BeautifulSoup
# 引用BeautifulSoup库

html = requests.get('http://books.toscrape.com/catalogue/category/books/travel_2/index.html')
# 获取数据
soup = BeautifulSoup(html.text,'html.parser')
# 解析数据
book_info_list = []
book_parent_list = soup.find_all('article',class_='product_pod')

for item in book_parent_list:
    rating = item.find('p')['class'][1]
    print(rating)
    name = item.find('h3').find('a').text
    print(name)
    price = item.find('div', class_='product_price').find('p').text
    print(price)
    book_info_list.append([name, price, rating])