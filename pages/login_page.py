"""Page Object для страницы логина"""

import allure
from pages.base_page import BasePage
from utils.locators import LoginPageLocators as Locators


class LoginPage(BasePage):
    """Страница авторизации"""
    
    @allure.step("Авторизоваться")
    def login(self, email: str, password: str):
        self.send_keys(Locators.EMAIL_INPUT, email)
        self.send_keys(Locators.PASSWORD_INPUT, password)
        self.click(Locators.LOGIN_BUTTON)