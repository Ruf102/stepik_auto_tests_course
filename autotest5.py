from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def celc(x):
    return math.log(abs(12*math.sin(x)))


try:
    link = 'https://suninjuly.github.io/execute_script.html'
    browser = webdriver.Chrome()
    browser.get(link)
    x = browser.find_element(By.ID, 'input_value').text
    input1 = browser.find_element(By.ID, 'answer')
    y = celc(int(x))
    browser.execute_script("return window.scrollBy(0, 100);")
    input1.send_keys(str(y))
    browser.find_element(By.ID, 'robotCheckbox').click()
    browser.find_element(By.ID, 'robotsRule').click()
    browser.find_element(By.CLASS_NAME, 'btn.btn-primary').click()







finally:
    time.sleep(5)
    browser.quit()