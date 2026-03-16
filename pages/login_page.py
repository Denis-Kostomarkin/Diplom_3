"""Page Object для страницы логина"""

import allure
from pages.base_page import BasePage
from utils.locators import LoginPageLocators as Locators
from utils.locators import MainPageLocators


class LoginPage(BasePage):
    """Страница авторизации"""
    
    @allure.step("Авторизоваться")
    def login(self, email: str, password: str):
        self.send_keys(Locators.EMAIL_INPUT, email)
        self.send_keys(Locators.PASSWORD_INPUT, password)
        self.click(Locators.LOGIN_BUTTON)

    @allure.step("Авторизоваться через главную страницу")
    def authorize_from_main_page(self, main_page, email: str, password: str):
        main_page.open_main_page()
        main_page.click(MainPageLocators.PERSONAL_CABINET_BUTTON)
        self.login(email, password)
        self.wait_for_url_not_contains("login")