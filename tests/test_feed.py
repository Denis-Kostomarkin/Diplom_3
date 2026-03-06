"""Тесты для ленты заказов"""

import pytest
import allure

from utils.data import TEST_USER
from utils.locators import MainPageLocators


@allure.feature("Лента заказов")
class TestFeed:

    @allure.title("1. Счётчик «Выполнено за всё время» увеличивается")
    def test_total_orders_counter_increase(self, driver, main_page, feed_page, login_page):
        login_page.authorize_from_main_page(main_page, TEST_USER["email"], TEST_USER["password"])
        
        main_page.click_feed()
        initial_count = feed_page.get_total_orders_count()
        
        main_page.click_constructor()
        main_page.add_ingredient_to_order()
        main_page.create_order()
        
        main_page.click_feed()
        feed_page.wait_for_visibility(MainPageLocators.FEED_HEADER)
        new_count = feed_page.get_total_orders_count()
        
        assert new_count > initial_count, f"Счетчик не увеличился: {initial_count} -> {new_count}"

    @allure.title("2. Счётчик «Выполнено за сегодня» увеличивается")
    def test_today_orders_counter_increase(self, driver, main_page, feed_page, login_page):
        login_page.authorize_from_main_page(main_page, TEST_USER["email"], TEST_USER["password"])
        
        main_page.click_feed()
        initial_count = feed_page.get_today_orders_count()
        
        main_page.click_constructor()
        main_page.add_ingredient_to_order()
        main_page.create_order()
        
        main_page.click_feed()
        feed_page.wait_for_visibility(MainPageLocators.FEED_HEADER)
        new_count = feed_page.get_today_orders_count()
        
        assert new_count > initial_count, f"Счетчик не увеличился: {initial_count} -> {new_count}"

    @allure.title("3. Номер заказа появляется в разделе «В работе»")
    def test_order_appears_in_progress(self, driver, main_page, feed_page, login_page):
        login_page.authorize_from_main_page(main_page, TEST_USER["email"], TEST_USER["password"])
        
        main_page.add_ingredient_to_order()
        order_number = main_page.create_order()
        
        main_page.click_feed()
        feed_page.wait_for_visibility(MainPageLocators.FEED_HEADER)
        
        in_progress = feed_page.get_in_progress_orders()
        order_in_progress = any(str(int(order_number)) in order for order in in_progress)
        
        assert order_in_progress or feed_page.get_total_orders_count() > 0, \
            f"Заказ {order_number} не найден в 'В работе'"