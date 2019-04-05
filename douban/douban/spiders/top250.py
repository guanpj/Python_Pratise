import scrapy
import bs4
from ..items import DoubanItem

class DoubanSpider(scrapy.Spider):
    name = 'douban'
    allowed_domains = ['https://book.douban.com']
    start_urls = []
    for i in range(3):
        url = 'https://book.douban.com/top250?start=' + str(i*25)
        start_urls.append(url)

    def parse(self, response):
        soup = bs4.BeautifulSoup(response.text, 'html.parser')
        tr_list = soup.find_all('tr', class_ = 'item')
        for tr in tr_list:
            item = DoubanItem()
            item['title'] = tr.find_all('a')[1]['title']
            item['publish'] = tr.find('p',class_='pl').text
            item['score'] = tr.find('span',class_='rating_nums').text
            print(item['title'])
            yield item