from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def test_registration_form(url):
    try:
        browser = webdriver.Chrome()
        browser.get(url)

        # Уникальные и точные селекторы только для обязательных полей
        input1 = browser.find_element(By.CSS_SELECTOR, "input[placeholder='Input your first name'][required]")
        input1.send_keys("Ivan")

        input2 = browser.find_element(By.CSS_SELECTOR, "input[placeholder='Input your last name'][required]")
        input2.send_keys("Petrov")

        input3 = browser.find_element(By.CSS_SELECTOR, "input[placeholder='Input your email'][required]")
        input3.send_keys("ivan.petrov@example.com")

        # Кнопка отправки формы
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        # Ожидание и проверка текста
        time.sleep(1)
        success_text = browser.find_element(By.TAG_NAME, "h1").text
        assert "Congratulations! You have successfully registered!" in success_text

        print(f"✅ Тест на {url} пройден успешно.")

    except Exception as e:
        print(f"❌ Тест на {url} не пройден. Ошибка: {type(e).__name__} - {e}")

    finally:
        time.sleep(3)
        browser.quit()

# Тест на обеих страницах
test_registration_form("http://suninjuly.github.io/registration1.html")
test_registration_form("http://suninjuly.github.io/registration2.html")
