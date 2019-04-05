from gevent import monkey
monkey.patch_all()
#让程序变成异步模式。
import gevent,requests,csv
from bs4 import BeautifulSoup
from gevent.queue import Queue 

work = Queue()
csv_file= open('Boohee.csv', 'w', newline='', encoding='utf-8')
writer = csv.writer(csv_file)
writer.writerow(['食物', '热量', '链接'])

for i in range(10):
    for j in range(5):
        work.put_nowait('http://www.boohee.com/food/group/%s?page=%s' % (i + 1, j + 1))

for j in range(5):
        work.put_nowait('http://www.boohee.com/food/group/view_menu?page=%s' % (j + 1))  


def clawer():
    headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'
    }
    while not work.empty():
        url = work.get_nowait()
        req = requests.get(url, headers=headers)
        soup = BeautifulSoup(req.text, 'html.parser')
        div_list = soup.find_all('div', class_='text-box pull-left')
        for div in div_list:
            food_name = div.find('a').text
            food_url = 'http://www.boohee.com' + div.find('a')['href']
            food_energy = div.find('p').text
            writer.writerow([food_name, food_energy, food_url])

task_list = []

for i in range(8):
    task = gevent.spawn(clawer())
    task_list.append(task)

gevent.joinall(task_list)

        