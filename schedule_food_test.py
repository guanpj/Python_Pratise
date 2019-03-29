import smtplib 
import requests
import schedule
import time
from bs4 import BeautifulSoup
from email.mime.text import MIMEText
from email.header import Header

def getFood():
    res_foods = requests.get('http://www.xiachufang.com/explore/')
    bs_foods = BeautifulSoup(res_foods.text,'html.parser')
    list_foods = bs_foods.find_all('div',class_='info pure-u')
    list_all = []
    for food in list_foods:
        tag_a = food.find('a')
        name = tag_a.text[17:-13]
        URL = 'http://www.xiachufang.com'+tag_a['href']
        tag_p = food.find('p',class_='ing ellipsis')
        ingredients = tag_p.text[1:-1]
        list_all.append([name,ingredients,URL])
    content=''
    for food_item in list_all:
        content += ('菜品 %s —— %s ：原料：%s ，详情：%s \n' % (list_all.index(food_item) + 1, food_item[0], food_item[1], food_item[2]))
    return list_all
    

receivers = ['409026844@qq.com','784998824@qq.com']

def sendMail(list_foods):
    mailhost='smtp.qq.com'
    qqmail = smtplib.SMTP()
    qqmail.connect(mailhost,25)

    account = '409026844@qq.com'
    password = 'hfduhmhfteklbhci'
    qqmail.login(account,password)

    content = '今日菜单：\n'
    for food_item in list_foods:
        content += ('菜品 %s —— %s ：原料：%s ，详情：%s \n' % (list_foods.index(food_item) + 1, food_item[0], food_item[1], food_item[2]))

    message = MIMEText(content, 'plain', 'utf-8')
    message['From'] = Header(account)
    message['To'] = Header(",".join(receivers))
    subject = '今日菜单'
    message['Subject'] = Header(subject, 'utf-8')

    try:
        qqmail.sendmail(account, receivers, message.as_string())
        print ('邮件发送成功')
    except:
        print ('邮件发送失败')
    qqmail.quit()


def job():
    sendMail(getFood())

schedule.every().day.at("13:40").do(job)

while(True):
    schedule.run_pending()
    time.sleep(1)