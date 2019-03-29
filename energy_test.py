from gevent import monkey
monkey.patch_all()
#让程序变成异步模式。
import gevent,requests,csv
from bs4 import BeautifulSoup
from gevent.queue import Queue 

work = Queue()

for i in range(10):
    work.put_nowait('http://www.boohee.com/food/group/1?page=' + (i + 1))
work.put_nowait('http://www.boohee.com/food/view_menu')

def clawer():
    while not work.empty():
        url = work.get_nowait()
        req = requests.get(url)
        soup = BeautifulSoup(req.text, 'html.parser')
        li_list = soup.find_all('li', class_='item clearfix')
        print(li_list)