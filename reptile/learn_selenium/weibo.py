from selenium import webdriver
import time

driver = webdriver.Chrome()

driver.get('https://weibo.com/')

time.sleep(10)

driver.find_element_by_id("loginname").send_keys('15901060580')
print(1)
driver.find_element_by_name("password").send_keys('')
print(2)
driver.find_element_by_class_name("W_btn_a").click()
print(3)
