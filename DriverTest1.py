from selenium.webdriver.chrome.webdriver import RemoteWebDriver # 从selenium库中调用RemoteWebDriver模块
from selenium.webdriver.chrome.options import Options # 从options模块中调用Options类
import time
from selenium import  webdriver 
from bs4 import BeautifulSoup

chrome_options = Options() # 实例化Option对象
chrome_options.add_argument('--headless') # 对浏览器的设置
# driver = RemoteWebDriver("http://chromedriver.python-class-fos.svc:4444/wd/hub", chrome_options.to_capabilities()) # 声明浏览器对象
#driver = webdriver.Chrome(options = chrome_options) 
driver = webdriver.Chrome()

driver.get('https://wordpress-edu-3autumn.localprod.forc.work/wp-login.php') # 访问页面
time.sleep(2)

name = driver.find_element_by_id('user_login')
name.send_keys("spiderman")
time.sleep(1)
psw = driver.find_element_by_id('user_pass')
psw.send_keys("crawler334566")
btn = driver.find_element_by_id('wp-submit')
btn.click()

time.sleep(2) # 等待两秒

target = driver.find_element_by_partial_link_text('同九义何汝');
driver.get(target.get_attribute("href"))
time.sleep(2)
box = driver.find_element_by_id('comment')
box.send_keys('selenium 牛逼' + input("请输入评论："))
time.sleep(1)
submit = driver.find_element_by_id("submit")
submit.click()

driver.close() # 关闭浏览器 # 关闭浏览器