import requests, csv
from bs4 import BeautifulSoup

url = 'http://www.mtime.com/top/tv/top100/index-2.html'
req = requests.get(url)
soup = BeautifulSoup(req.text, 'html.parser')
h2_list = soup.find_all("h2", class_ = "px14 pb6")
cvs_file = open("Top10.csv", 'w', newline='', encoding='utf-8')
writer = csv.writer(cvs_file)
for h2 in h2_list:
    name = h2.find('a').text
    writer.writerow(name)
cvs_file.close()