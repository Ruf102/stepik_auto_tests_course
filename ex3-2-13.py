import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class Test11(unittest.TestCase):
    def test1(self):
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)

        input1 = browser.find_element(By.XPATH, '//div[@class="first_block"]//input[@class="form-control first"]')
        input1.send_keys('Иван')

        input2 = browser.find_element(By.XPATH, '//div[@class="first_block"]//input[@class="form-control second"]')
        input2.send_keys('Иванов')

        input3 = browser.find_element(By.XPATH, '//div[@class="first_block"]//input[@class="form-control third"]')
        input3.send_keys('t@t.ru')



        # Отправляем заполненную форму
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        end_text = 'Congratulations! You have successfully registered!'
        self.assertEqual(welcome_text, end_text,
                         f"Фактический текст {welcome_text} не соответствует ожидаемому {end_text}")

    def test2(self):
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)

        input1 = browser.find_element(By.XPATH, '//div[@class="first_block"]//input[@class="form-control first"]')
        input1.send_keys('Иван')

        input2 = browser.find_element(By.XPATH, '//div[@class="first_block"]//input[@class="form-control second"]')
        input2.send_keys('Иванов')

        input3 = browser.find_element(By.XPATH, '//div[@class="first_block"]//input[@class="form-control third"]')
        input3.send_keys('t@t.ru')



        # Отправляем заполненную форму
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        end_text = 'Congratulations! You have successfully registered!'
        self.assertEqual(welcome_text, end_text,
                         f"Фактический текст {welcome_text} не соответствует ожидаемому {end_text}")

if __name__ == "__main__":
    unittest.main()