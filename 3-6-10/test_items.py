from selenium.webdriver.common.by import By

def test_add_button(browser):
    link = 'https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207'
    browser.get(link)
    button = browser.find_element(By.CLASS_NAME, 'btn.btn-lg.btn-primary.btn-add-to-basket')
    assert button, "Кнопка добавления в корзину не найдена на странице"