from selenium import webdriver
import time

# selenium 的 headless 模式
#导入 Options 方法
from selenium.webdriver.chrome.options import Options

#实例化 Options对象
chrome_options = Options()

#为 自定义的对象添加参数
chrome_options.add_argument('--headless')
chrome_options.add_argument("window-size=1980,1080")

#将自定义的参数添加到实例化Chrome时的参数里
driver = webdriver.Chrome(chrome_options=chrome_options)

driver.get('http://www.baidu.com')

driver.find_element_by_id('kw').send_keys('小骚逼')

driver.find_element_by_id('su').click()

cookie= driver.get_cookies()

print(cookie)
