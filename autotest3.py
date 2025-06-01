from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


def celc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = 'https://suninjuly.github.io/get_attribute.html'
    browser = webdriver.Chrome()
    browser.get(link)
    box = browser.find_element(By.CSS_SELECTOR, '[src="images/chest.png"]')
    y = celc(box.get_attribute('valuex'))
    input1 = browser.find_element(By.ID, 'answer')
    input1.send_keys(y)
    check_box = browser.find_element(By.ID, 'robotCheckbox')
    check_box.click()
    radio_button = browser.find_element(By.ID, 'robotsRule')
    radio_button.click()
    submit = browser.find_element(By.CSS_SELECTOR, '[class="btn btn-default"]')
    submit.click()



finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()