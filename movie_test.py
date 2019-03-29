import requests, random, bs4, openpyxl, csv

csv_file = open("Movie1.csv", "w", newline='',encoding='utf-8')

writer = csv.writer(csv_file)
writer.writerow(['排名','电影名称','评分','评分','链接'])


for x in range(10):
    url = 'https://movie.douban.com/top250?start=' + str(x*25) + '&filter='
    res = requests.get(url)
    bs = bs4.BeautifulSoup(res.text, 'html.parser')
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
        print(num + '.' + title + '——' + comment + '\n' + '推荐语：' + tes +'\n' + url_movie)

csv_file.close()


