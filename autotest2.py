from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = 'https://suninjuly.github.io/math.html'
    browser = webdriver.Chrome()
    browser.get(link)
    element_x = browser.find_element(By.ID, 'input_value')
    x = element_x.text
    y = calc(x)
    input1 = browser.find_element(By.ID, 'answer')
    input1.send_keys(y)
    check_box = browser.find_element(By.CLASS_NAME, 'form-check-input')
    check_box.click()
    option1 = browser.find_element(By.CSS_SELECTOR, '[for="robotsRule"]')
    option1.click()
    button_submit = browser.find_element(By.CLASS_NAME, 'btn.btn-default')
    button_submit.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()