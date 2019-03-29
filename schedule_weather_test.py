import smtplib 
import requests
import schedule
import time
from bs4 import BeautifulSoup
from email.mime.text import MIMEText
from email.header import Header

def getTemAndWeather():
    headers={'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}
    url='http://www.weather.com.cn/weather/101280601.shtml'
    res=requests.get(url,headers=headers)
    res.encoding='utf-8'
    bsdata=BeautifulSoup(res.text,'html.parser')
    data1= bsdata.find(class_='tem')
    data2= bsdata.find(class_='wea')
    return data1.text, data2.text

def sendMail(tem, wea, receiver="409026844@qq.com"):
    mailhost='smtp.qq.com'
    qqmail = smtplib.SMTP()
    qqmail.connect(mailhost,25)

    account = '409026844@qq.com'
    password = 'hfduhmhfteklbhci'
    qqmail.login(account,password)

    content = '今天的天气： ' + tem +  wea
    message = MIMEText(content, 'plain', 'utf-8')
    subject = '今日天气预报'
    message['Subject'] = Header(subject, 'utf-8')

    try:
        qqmail.sendmail(account, receiver, message.as_string())
        print ('邮件发送成功')
    except:
        print ('邮件发送失败')
    qqmail.quit()

def job():
    tem, wea = getTemAndWeather()
    sendMail(tem, wea)

schedule.every().day.at("11:00").do(job)
while(True):
    schedule.run_pending()
    time.sleep(1)