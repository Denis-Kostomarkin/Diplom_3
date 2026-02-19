"""Базовый класс для всех страниц"""

import allure
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    """Базовый класс страницы"""
    
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    @allure.step("Открыть страницу {url}")
    def open(self, url: str):
        self.driver.get(url)

    @allure.step("Найти элемент {locator}")
    def find_element(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    @allure.step("Кликнуть по элементу {locator}")
    def click(self, locator):
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()

    @allure.step("Ввести текст в элемент {locator}")
    def send_keys(self, locator, text: str):
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)

    @allure.step("Получить текст элемента {locator}")
    def get_text(self, locator):
        return self.find_element(locator).text

    @allure.step("Проверить видимость элемента {locator}")
    def is_visible(self, locator):
        try:
            return self.find_element(locator).is_displayed()
        except:
            return False

    @allure.step("Подождать исчезновения элемента {locator}")
    def wait_for_invisibility(self, locator):
        return self.wait.until(EC.invisibility_of_element_located(locator))

    @allure.step("Прокрутить к элементу {locator}")
    def scroll_to_element(self, locator):
        """Прокрутить страницу к элементу"""
        element = self.find_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", element)