"""Тесты для конструктора бургера"""

import pytest
import allure

from utils.locators import MainPageLocators


@allure.feature("Конструктор бургера")
class TestConstructor:

    @allure.title("1. Переход по клику на «Конструктор»")
    def test_click_constructor_button(self, driver, main_page):
        main_page.open_main_page()
        
        main_page.click_feed()
        main_page.click_constructor()
        
        assert main_page.is_constructor_header_displayed(), "Заголовок конструктора не отображается"

    @allure.title("2. Переход по клику на «Лента заказов»")
    def test_click_feed_button(self, driver, main_page):
        main_page.open_main_page()
        main_page.click_feed()
        
        assert main_page.is_visible(MainPageLocators.FEED_HEADER), "Заголовок ленты не отображается"

    @allure.title("3. Появление всплывающего окна с деталями ингредиента")
    def test_ingredient_details_modal(self, driver, main_page):
        main_page.open_main_page()
        main_page.click_ingredient()
        
        assert main_page.is_ingredient_modal_displayed(), "Модальное окно не открылось"

    @allure.title("4. Закрытие всплывающего окна по крестику")
    def test_close_ingredient_modal(self, driver, main_page):
        main_page.open_main_page()
        main_page.click_ingredient()
        
        assert main_page.is_ingredient_modal_displayed(), "Модальное окно не открылось"
        
        main_page.close_ingredient_modal()
        
        assert main_page.wait_for_invisibility(MainPageLocators.INGREDIENT_DETAILS_MODAL), "Модальное окно не закрылось"

    @allure.title("5. Увеличение счётчика при добавлении ингредиента")
    def test_ingredient_counter_increase(self, driver, main_page):
        main_page.open_main_page()
        
        initial_count = main_page.get_ingredient_counter()
        main_page.add_ingredient_to_order()
        new_count = main_page.get_ingredient_counter()
        
        assert new_count > initial_count, f"Счетчик не увеличился: {initial_count} -> {new_count}"