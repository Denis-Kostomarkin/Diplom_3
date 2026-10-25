"""Page Object для страницы ленты заказов"""

import allure
import re
from selenium.webdriver.support.ui import WebDriverWait
from pages.base_page import BasePage
from utils.locators import FeedPageLocators as Locators


class FeedPage(BasePage):
    """Страница ленты заказов"""
    
    @staticmethod
    def _missing_counter(text):
        raise ValueError(f"Не удалось прочитать счётчик из текста: {text!r}")

    def wait_for_counter_increase(self, getter, previous, timeout=20):
        return WebDriverWait(self.driver, timeout).until(
            lambda _: getter() > previous,
            message=f"Счётчик не увеличился относительно {previous}",
        )

    @allure.step("Получить счетчик 'Выполнено за все время'")
    def get_total_orders_count(self):
        text = self.get_text(Locators.TOTAL_ORDERS_COUNTER)
        numbers = re.findall(r'\d+', text.replace(' ', ''))
        return int(numbers[0]) if numbers else self._missing_counter(text)

    @allure.step("Получить счетчик 'Выполнено за сегодня'")
    def get_today_orders_count(self):
        text = self.get_text(Locators.TODAY_ORDERS_COUNTER)
        numbers = re.findall(r'\d+', text.replace(' ', ''))
        return int(numbers[0]) if numbers else 0

    @allure.step("Получить заказы 'В работе'")
    def get_in_progress_orders(self):
        """Получить список заказов в работе"""
        orders = self.find_elements(Locators.IN_PROGRESS_ORDERS)
        return [order.text.strip() for order in orders if order.text.strip()]

    @allure.step("Проверить наличие заказа в 'В работе'")
    def is_order_in_progress(self, order_number):
        orders = self.get_in_progress_orders()
        order_num_str = str(int(order_number))
        return any(order.strip().lstrip('#').strip() == order_num_str for order in orders)