import pytest
from selenium import webdriver

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default="chrome",
                     help="language browser: Any language")

@pytest.fixture()
def language(request):
    language = request.config.getoption("language")
    return language

@pytest.fixture()
def browser():
    browser = webdriver.Chrome()
    yield browser
    browser.quit()

