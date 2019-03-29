from gevent import monkey
monkey.patch_all()
import gevent, time, requests, csv
from gevent.queue import Queue
from bs4 import BeautifulSoup

work = Queue()

cvs_file = open("Top100.csv", 'w', newline='', encoding='utf-8')

for i in range(10):
    if i == 0:
        work.put_nowait('http://www.mtime.com/top/tv/top100/index.html')
    else:
        url = 'http://www.mtime.com/top/tv/top100/index-%s.html' % (i + 1)
        work.put_nowait(url)

print(work.qsize())

def crawler():
    while not work.empty():
        url = work.get_nowait()
        req = requests.get(url)
        soup = BeautifulSoup(req.text, 'html.parser')
        h2_list = soup.find_all("h2", class_ = "px14 pb6")
        
        writer = csv.writer(cvs_file)
        for h2 in h2_list:
            name = h2.find('a').text
            writer.writerow([name])
        

task_list = []

for i in range(3):
    task = gevent.spawn(crawler)
    task_list.append(task)

gevent.joinall(task_list)

cvs_file.close()

