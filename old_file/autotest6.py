from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

current_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(current_dir, 'file.txt')

try:
    link = 'http://suninjuly.github.io/file_input.html'
    browser = webdriver.Chrome()
    browser.get(link)
    input_name = browser.find_element(By.CSS_SELECTOR, '[name="firstname"]')
    input_name.send_keys('Иван')
    input_lastname = browser.find_element(By.CSS_SELECTOR, '[name="lastname"]')
    input_lastname.send_keys('Иванов')
    input_email = browser.find_element(By.CSS_SELECTOR, '[name="email"]')
    input_email.send_keys('t@t.ru')
    file_op = browser.find_element(By.ID, 'file')
    file_op.send_keys(file_path)
    browser.find_element(By.CLASS_NAME, 'btn.btn-primary').click()

finally:
    time.sleep(5)
    browser.quit()