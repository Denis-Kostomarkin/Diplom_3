"""Page Object для главной страницы"""

import allure
import time
from selenium.webdriver.common.action_chains import ActionChains

from pages.base_page import BasePage
from utils.locators import MainPageLocators as Locators
from utils.data import BASE_URL


class MainPage(BasePage):
    """Главная страница Stellar Burgers"""
    
    @allure.step("Открыть главную страницу")
    def open_main_page(self):
        self.open(BASE_URL)

    @allure.step("Кликнуть на 'Конструктор'")
    def click_constructor(self):
        self.click(Locators.CONSTRUCTOR_BUTTON)

    @allure.step("Кликнуть на 'Лента заказов'")
    def click_feed(self):
        self.click(Locators.FEED_BUTTON)

    @allure.step("Кликнуть на ингредиент")
    def click_ingredient(self, locator=Locators.INGREDIENT_BUN):
        self.click(locator)

    @allure.step("Закрыть модальное окно ингредиента")
    def close_ingredient_modal(self):
        time.sleep(0.5)
        self.click(Locators.INGREDIENT_DETAILS_CLOSE)

    @allure.step("Добавить ингредиент в заказ")
    def add_ingredient_to_order(self, locator=Locators.INGREDIENT_BUN):
        """Drag-and-drop через ActionChains"""
        source = self.find_element(locator)
        target = self.find_element(Locators.BURGER_CONSTRUCTOR_AREA)
        
        actions = ActionChains(self.driver)
        actions.click_and_hold(source)
        actions.move_to_element(target)
        actions.release(target)
        actions.perform()

    @allure.step("Получить значение счетчика ингредиента")
    def get_ingredient_counter(self):
        try:
            return int(self.get_text(Locators.CONSTRUCTOR_INGREDIENT_COUNTER))
        except:
            return 0

    @allure.step("Проверить отображение модального окна ингредиента")
    def is_ingredient_modal_displayed(self):
        time.sleep(0.5)
        return self.is_visible(Locators.INGREDIENT_DETAILS_MODAL)

    @allure.step("Проверить отображение заголовка конструктора")
    def is_constructor_header_displayed(self):
        return self.is_visible(Locators.CONSTRUCTOR_HEADER)

    @allure.step("Кликнуть 'Оформить заказ'")
    def click_order_button(self):
        self.click(Locators.ORDER_BUTTON)

    @allure.step("Получить номер заказа")
    def get_order_number(self):
        time.sleep(15)
        return self.get_text(Locators.ORDER_NUMBER)

    @allure.step("Закрыть модальное окно заказа")
    def close_order_modal(self):
        time.sleep(1)
        self.click(Locators.ORDER_MODAL_CLOSE)
        time.sleep(0.5)

    @allure.step("Оформить заказ")
    def create_order(self):
        self.click_order_button()
        order_number = self.get_order_number()
        self.close_order_modal()
        return order_number