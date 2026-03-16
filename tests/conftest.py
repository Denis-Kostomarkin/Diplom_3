"""Фикстуры для UI-тестов"""

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions

from pages.main_page import MainPage
from pages.feed_page import FeedPage
from pages.login_page import LoginPage


def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        default="chrome",
        help="Browser: chrome or firefox"
    )


@pytest.fixture
def driver(request):
    """Создание драйвера"""
    browser = request.config.getoption("--browser")
    
    if browser == "chrome":
        options = ChromeOptions()
        options.add_argument("--start-maximized")
        options.add_argument("--no-sandbox")
        
        driver = webdriver.Chrome(options=options)
        
    elif browser == "firefox":
        options = FirefoxOptions()
        options.add_argument("--width=1920")
        options.add_argument("--height=1080")
        
        driver = webdriver.Firefox(options=options)
    else:
        raise ValueError(f"Unsupported browser: {browser}")
    
    yield driver
    driver.quit()


@pytest.fixture
def main_page(driver):
    return MainPage(driver)


@pytest.fixture
def feed_page(driver):
    return FeedPage(driver)


@pytest.fixture
def login_page(driver):
    return LoginPage(driver)