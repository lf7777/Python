from selenium import webdriver
import time

driver = webdriver.Chrome()

driver.get('http://fanyi.youdao.com/')

driver.find_element_by_id('inputOriginal').send_keys('美女')

driver.find_element_by_id('transMachine').click()

#time.sleep(0.0000001)

translated = driver.find_element_by_id('transTarget').text

print(translated)
