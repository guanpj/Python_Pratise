import smtplib 
import requests
import schedule
import time, random, csv
from bs4 import BeautifulSoup
from email.mime.text import MIMEText
from email.header import Header
from urllib.request import quote

def getMovie():
    csv_file = open("MovieTop.csv", "w", newline='',encoding='utf-8')
    writer = csv.writer(csv_file)
    writer.writerow(['排名','电影名称','评分','评分','链接'])
    for x in range(10):
        url = 'https://movie.douban.com/top250?start=' + str(x*25) + '&filter='
        res = requests.get(url)
        bs = BeautifulSoup(res.text, 'html.parser')
        bs = bs.find('ol', class_="grid_view")
        for titles in bs.find_all('li'):
            num = titles.find('em',class_="").text
            #查找序号
            title = titles.find('span', class_="title").text
            #查找电影名
            print(titles.find('span',class_="inq"))
            if not titles.find('span',class_="inq") is None:
                tes = titles.find('span',class_="inq").text
            else:
                tes = '无'
            #查找推荐语
            comment = titles.find('span',class_="rating_num").text
            #查找评分
            url_movie = titles.find('a')['href']

            writer.writerow([num, title, comment, tes, url_movie])
    csv_file.close()


def getRandomMovie(count):
    with open('MovieTop.csv', 'r', newline='', encoding='utf-8') as f:
        reader = csv.reader(f)
        rows_list = list(reader)
        name_list= []
        for i in range(0, count):
            name_list.append(random.choice(rows_list)[1])
        return name_list

def getMovieDetail(name_list):
    for movie_name in name_list:
        gbkmovie = movie_name.encode('gbk')
        urlsearch = 'http://s.ygdy8.com/plus/so.php?typeid=1&keyword='+quote(gbkmovie)
        res = requests.get(urlsearch)
        search_soup = BeautifulSoup(res.text, 'html.parser')
        
