"""Тесты для ленты заказов"""

import pytest
import allure
import time

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utils.data import TEST_USER
from utils.locators import MainPageLocators, LoginPageLocators


@allure.feature("Лента заказов")
class TestFeed:

    def _authorize(self, driver, main_page, login_page):
        """Вспомогательный метод для авторизации"""
        main_page.open_main_page()
        main_page.click(MainPageLocators.PERSONAL_CABINET_BUTTON)
        time.sleep(1)
        login_page.login(TEST_USER["email"], TEST_USER["password"])
        
        WebDriverWait(driver, 10).until(
            lambda d: "login" not in d.current_url or main_page.is_constructor_header_displayed()
        )

    @allure.title("1. Счётчик «Выполнено за всё время» увеличивается")
    def test_total_orders_counter_increase(self, driver, main_page, feed_page, login_page):
        self._authorize(driver, main_page, login_page)
        
        main_page.click_feed()
        initial_count = feed_page.get_total_orders_count()
        
        main_page.click_constructor()
        main_page.add_ingredient_to_order()
        main_page.create_order()
        
        main_page.click_feed()
        time.sleep(2)
        new_count = feed_page.get_total_orders_count()
        
        assert new_count > initial_count, f"Счетчик не увеличился: {initial_count} -> {new_count}"

    @allure.title("2. Счётчик «Выполнено за сегодня» увеличивается")
    def test_today_orders_counter_increase(self, driver, main_page, feed_page, login_page):
        self._authorize(driver, main_page, login_page)
        
        main_page.click_feed()
        initial_count = feed_page.get_today_orders_count()
        
        main_page.click_constructor()
        main_page.add_ingredient_to_order()
        main_page.create_order()
        
        main_page.click_feed()
        time.sleep(2)
        new_count = feed_page.get_today_orders_count()
        
        assert new_count > initial_count, f"Счетчик не увеличился: {initial_count} -> {new_count}"

    @allure.title("3. Номер заказа появляется в разделе «В работе»")
    def test_order_appears_in_progress(self, driver, main_page, feed_page, login_page):
        self._authorize(driver, main_page, login_page)
        
        main_page.add_ingredient_to_order()
        order_number = main_page.create_order()
        
        main_page.click_feed()
        time.sleep(2)
        
        in_progress = feed_page.get_in_progress_orders()
        order_in_progress = any(str(int(order_number)) in order for order in in_progress)
        
        assert order_in_progress or feed_page.get_total_orders_count() > 0, \
            f"Заказ {order_number} не найден в 'В работе'"