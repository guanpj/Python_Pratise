import requests
# 引用requests库
from bs4 import BeautifulSoup
# 引用BeautifulSoup库

res_foods = requests.get('http://www.xiachufang.com/explore/')
# 获取数据
bs_foods = BeautifulSoup("abc",'html.parser')
# 解析数据
if not bs_foods.find('div',class_='info pure-u') is None:
    list_foods = bs_foods.find('div',class_='info pure-u').text
# 查找最小父级标签

result=list()

