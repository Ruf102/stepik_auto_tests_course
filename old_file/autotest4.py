from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

try:
    link = 'https://suninjuly.github.io/selects2.html'
    browser = webdriver.Chrome()
    browser.get(link)
    num1 = browser.find_element(By.ID, 'num1').text
    num2 = browser.find_element(By.ID, 'num2').text
    y = (int(num1) + int(num2))
    select = Select(browser.find_element(By.ID, 'dropdown'))
    select.select_by_visible_text(str(y))
    browser.find_element(By.CLASS_NAME, 'btn.btn-default').click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()