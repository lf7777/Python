from selenium import webdriver
import time

#实例化谷歌浏览器对象
driver = webdriver.Chrome()

#输入url,访问网页
driver.get('http://www.baidu.com')

#可通过id定位数据,填写了表单
driver.find_element_by_id('kw').send_keys('大长腿是什么体验')

#提交表单
driver.find_element_by_id('su').click()

time.sleep(3)

#获取网页源代码,并保存
with open('tmp.html','wb')as f:
    f.write(driver.page_source.encode('utf-8'))


