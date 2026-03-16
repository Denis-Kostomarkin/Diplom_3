"""Page Object для страницы ленты заказов"""

import allure
import re
from pages.base_page import BasePage
from utils.locators import FeedPageLocators as Locators


class FeedPage(BasePage):
    """Страница ленты заказов"""
    
    @allure.step("Получить счетчик 'Выполнено за все время'")
    def get_total_orders_count(self):
        text = self.get_text(Locators.TOTAL_ORDERS_COUNTER)
        numbers = re.findall(r'\d+', text.replace(' ', ''))
        return int(numbers[0]) if numbers else 0

    @allure.step("Получить счетчик 'Выполнено за сегодня'")
    def get_today_orders_count(self):
        text = self.get_text(Locators.TODAY_ORDERS_COUNTER)
        numbers = re.findall(r'\d+', text.replace(' ', ''))
        return int(numbers[0]) if numbers else 0

    @allure.step("Получить заказы 'В работе'")
    def get_in_progress_orders(self):
        """Получить список заказов в работе"""
        try:
            orders = self.find_elements(Locators.IN_PROGRESS_ORDERS)
            return [order.text for order in orders if order.text.strip()]
        except:
            return []

    @allure.step("Проверить наличие заказа в 'В работе'")
    def is_order_in_progress(self, order_number):
        orders = self.get_in_progress_orders()
        order_num_str = str(int(order_number))
        return any(order_num_str in order for order in orders)