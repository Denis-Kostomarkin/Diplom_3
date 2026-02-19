"""Локаторы для всех страниц"""

from selenium.webdriver.common.by import By


class MainPageLocators:
    # Навигация
    CONSTRUCTOR_BUTTON = (By.XPATH, "//p[text()='Конструктор']/parent::a")
    FEED_BUTTON = (By.XPATH, "//p[text()='Лента Заказов']/parent::a")
    PERSONAL_CABINET_BUTTON = (By.XPATH, "//p[text()='Личный Кабинет']/parent::a")
    
    # Заголовки
    CONSTRUCTOR_HEADER = (By.XPATH, "//h1[text()='Соберите бургер']")
    FEED_HEADER = (By.XPATH, "//h1[text()='Лента заказов']")
    
    # Ингредиенты
    INGREDIENT_BUN = (By.XPATH, "(//a[contains(@class, 'BurgerIngredient_ingredient__')])[1]")
    
    # Модальное окно
    INGREDIENT_DETAILS_MODAL = (By.XPATH, "//div[contains(@class, 'Modal_modal__contentBox')]")
    INGREDIENT_DETAILS_CLOSE = (By.XPATH, "//button[contains(@class, 'Modal_modal__close')]")
    INGREDIENT_NAME_IN_MODAL = (By.XPATH, "//div[contains(@class, 'Modal_modal__contentBox')]//h2")
    
    # Конструктор
    BURGER_CONSTRUCTOR_AREA = (By.XPATH, "//section[contains(@class, 'BurgerConstructor_basket__')]")
    CONSTRUCTOR_INGREDIENT_COUNTER = (By.XPATH, "(//div[contains(@class, 'counter_counter__')]//p)[1]")
    
    # Кнопка заказа
    ORDER_BUTTON = (By.XPATH, "//button[contains(text(), 'Оформить заказ')]")
    ORDER_MODAL = (By.XPATH, "//div[contains(@class, 'Modal_modal__container')]")
    ORDER_NUMBER = (By.XPATH, "//h2[contains(@class, 'Modal_modal__title')]")
    ORDER_MODAL_CLOSE = (By.XPATH, "//button[contains(@class, 'Modal_modal__close')]")


class FeedPageLocators:
    # Счетчики
    TOTAL_ORDERS_COUNTER = (By.XPATH, "//p[text()='Выполнено за все время:']/following-sibling::p")
    TODAY_ORDERS_COUNTER = (By.XPATH, "//p[text()='Выполнено за сегодня:']/following-sibling::p")
    
    # В работе
    IN_PROGRESS_SECTION = (By.XPATH, "//p[text()='В работе:']/following-sibling::ul")
    IN_PROGRESS_ORDERS = (By.XPATH, "//p[text()='В работе:']/following-sibling::ul/li")


class LoginPageLocators:
    EMAIL_INPUT = (By.XPATH, "//label[text()='Email']//following-sibling::input")
    PASSWORD_INPUT = (By.XPATH, "//input[@type='password']")
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти']")