import scrapy
import bs4
from ..items import DangdangItem

class DangdangSpider(scrapy.Spider):
    name = 'dangdang'
    allowed_domains = ['http://bang.dangdang.com']
    start_urls = []
    for i in range(3):
        url = 'http://bang.dangdang.com/books/bestsellers/01.00.00.00.00.00-year-2018-0-1-' + str(i+1)
        start_urls.append(url)

    def parse(self, response):
        soup = bs4.BeautifulSoup(response.text, 'html.parser')
        li_list = soup.find('ul', class_ = 'bang_list clearfix bang_list_mode').find_all('li')
        for li in li_list:
            item = DangdangItem()
            item['num'] = li.find('div', class_ = 'list_num').text[:-1]
            item['name'] = li.find('div', class_ = 'name').find('a')['title']
            yield item