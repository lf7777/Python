from selenium import webdriver
import time

driver = webdriver.Chrome()

driver.get('https://www.jd.com/')

driver.find_element_by_id('key').send_keys('宏远食品专营店')

driver.find_elements_by_css_selector('.button')[0].click()

time.sleep(3)

driver.find_elements_by_css_selector('.p-o-btn')[2].click()
