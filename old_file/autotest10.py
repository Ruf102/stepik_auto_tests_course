import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math

def cecl(x):
    return math.log(abs(12*math.sin(x)))

try:
    link = 'http://suninjuly.github.io/explicit_wait2.html'
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    browser.get(link)
    WebDriverWait(browser, 13).until(EC.text_to_be_present_in_element((By.ID, 'price'), '100'))
    browser.find_element(By.ID, 'book').click()
    x = browser.find_element(By.ID, 'input_value').text
    y = cecl(int(x))
    input_result = browser.find_element(By.ID, 'answer')
    input_result.send_keys(y)
    browser.find_element(By.ID, 'solve').click()


finally:
    time.sleep(5)
    browser.quit()