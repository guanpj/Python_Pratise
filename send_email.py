import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.header import Header

# smtplib
import smtplib

from_addr = '409026844@qq.com'
password = 'hfduhmhfteklbhci'

to_addrs = ['409026844@qq.com','784998824@qq.com']
to_addr = '784998824@qq.com'

smtp_server = 'smtp.qq.com'

server = smtplib.SMTP_SSL(smtp_server)
server.connect(smtp_server,465)
server.login(from_addr, password)
text = '''
老婆老婆我爱你
'''
msg = MIMEText(text,'plain','utf-8')
msg['From'] = Header(from_addr)
msg['To'] = Header(",".join(to_addrs))
msg['Subject'] = Header('python test')
server.sendmail(from_addr, to_addrs, msg.as_string())
server.quit()