from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def cecl(x):
    return math.log(abs(12*math.sin(x)))

try:
    link = 'https://suninjuly.github.io/alert_accept.html'
    browser = webdriver.Chrome()
    browser.get(link)
    browser.find_element(By.CLASS_NAME, 'btn.btn-primary').click()
    browser.switch_to.alert.accept()
    x = browser.find_element(By.ID, 'input_value').text
    y = cecl(int(x))
    input_result = browser.find_element(By.ID, 'answer')
    input_result.send_keys(y)
    browser.find_element(By.CLASS_NAME, 'btn.btn-primary').click()



finally:
    time.sleep(5)