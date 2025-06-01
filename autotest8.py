from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def cecl(x):
    return math.log(abs(12*math.sin(x)))

try:
    link = 'http://suninjuly.github.io/redirect_accept.html'
    browser = webdriver.Chrome()
    browser.get(link)
    browser.find_element(By.CLASS_NAME, 'trollface.btn.btn-primary').click()
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
    x = browser.find_element(By.ID, 'input_value').text
    y = cecl(int(x))
    input_result = browser.find_element(By.ID, 'answer')
    input_result.send_keys(y)
    browser.find_element(By.CLASS_NAME, 'btn.btn-primary').click()



finally:
    time.sleep(5)