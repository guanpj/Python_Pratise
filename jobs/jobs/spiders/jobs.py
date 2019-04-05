import scrapy  
import bs4
from ..items import JobsItem

class JobSpider(scrapy.Spider):
    name = 'jobs'
    allowed_domains = ['www.jobui.com']
    start_urls = ['https://www.jobui.com/rank/company/']

    def parse(self, response):
        soup = bs4.BeautifulSoup(response.text, 'html.parser')
        ul_list = soup.find_all('ul', class_ = 'textList flsty cfix')
        for ul in ul_list:
            a_list = ul.find_all('a')
            for a in a_list:
                company_id = a['href']
                url = 'https://www.jobui.com{id}jobs'
                real_url = url.format(id=company_id)
                yield scrapy.Request(real_url, callback = self.parse_job)

    def parse_job(self, response):
        bs = bs4.BeautifulSoup(response.text, 'html.parser')
        company = bs.find(id="companyH1").text
        li_list = bs.find_all('li',class_="company-job-list")
        for li in li_list:
            item = JobsItem()
            item['company'] = company
            item['position']= li.find('h3').find('a').text
            item['address'] = li.find('span',class_="col80").text
            item['detail'] = li.find('span',class_="col150").text
            yield item