import requests, random, bs4

num_list=[]
title_list=[]
tes_list=[]
commnent_list=[]
url_list=[]

movie_info_list = []

for x in range(10):
    url = 'https://movie.douban.com/top250?start=' + str(x*25) + '&filter='
    res = requests.get(url)
    bs = bs4.BeautifulSoup(res.text, 'html.parser')
    bs = bs.find('ol', class_="grid_view")
    for titles in bs.find_all('li'):
        num = titles.find('em',class_="").text
        num_list.append(num)
        #查找序号
        title = titles.find('span', class_="title").text
        title_list.append(title)
        #查找电影名
        print(titles.find('span',class_="inq"))
        if not titles.find('span',class_="inq") is None:
            tes = titles.find('span',class_="inq").text
            tes_list.append(tes)
        else:
            tes_list.append('无')
        #查找推荐语
        comment = titles.find('span',class_="rating_num").text
        commnent_list.append(comment)
        #查找评分
        url_movie = titles.find('a')['href']
        url_list.append(url_movie)

        print(num + '.' + title + '——' + comment + '\n' + '推荐语：' + tes +'\n' + url_movie)

for i in range(len(num_list)):
    movie_info_list.append([num_list[i], title_list[i], tes_list[i], commnent_list[i], url_list[i]])

print(movie_info_list)