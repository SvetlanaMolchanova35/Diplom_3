from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class MainPage(BasePage):
    
    @allure.step("Нажать на кнопку 'Конструктор'")
    def click_constructor_button(self):
        """Кликнуть на кнопку конструктора"""
        self.click_element(MainPageLocators.CONSTRUCTOR_BUTTON)
        self.wait_for_page_load()
    
    @allure.step("Нажать на кнопку 'Лента заказов'")
    def click_order_feed_button(self):
        """Кликнуть на кнопку ленты заказов"""
        self.click_element(MainPageLocators.ORDER_FEED_BUTTON)
        self.wait_for_page_load()
    
    @allure.step("Нажать на кнопку 'Личный кабинет'")
    def click_personal_account_button(self):
        """Кликнуть на кнопку личного кабинета"""
        self.click_element(MainPageLocators.PERSONAL_ACCOUNT_BUTTON)
    
    @allure.step("Кликнуть на первый ингредиент")
    def click_first_ingredient(self):
        """Кликнуть на первый доступный ингредиент"""
        self.click_element(MainPageLocators.INGREDIENT_ITEM)
    
    @allure.step("Получить название ингредиента из модального окна")
    def get_ingredient_name_from_modal(self):
        """Получить название ингредиента из модального окна"""
        return self.get_text(MainPageLocators.INGREDIENT_DETAILS_NAME)
    
    @allure.step("Закрыть модальное окно")
    def close_modal(self):
        """Закрыть модальное окно"""
        self.click_element(MainPageLocators.MODAL_CLOSE_BUTTON)
        self.wait_for_invisibility(MainPageLocators.MODAL_OVERLAY)
    
    @allure.step("Проверить, что модальное окно открыто")
    def is_modal_visible(self):
        """Проверить видимость модального окна"""
        return self.is_element_visible(MainPageLocators.MODAL_OVERLAY)
    
    @allure.step("Получить счетчик первого ингредиента")
    def get_first_ingredient_counter(self):
        """Получить значение счетчика первого ингредиента"""
        try:
            counter_element = self.find_element(MainPageLocators.INGREDIENT_COUNTER, timeout=3)
            counter_text = counter_element.text
            return int(counter_text) if counter_text.isdigit() else 0
        except:
            return 0
    
    @allure.step("Добавить ингредиент в конструктор")
    def add_ingredient_to_constructor(self):
        """Добавить ингредиент через drag and drop"""
        ingredient = self.find_element(MainPageLocators.INGREDIENT_ITEM)
        constructor = self.find_element(MainPageLocators.CONSTRUCTOR_AREA)
        
        # Используем JavaScript для drag and drop
        self.driver.execute_script("""
            var dataTransfer = new DataTransfer();
            arguments[0].dispatchEvent(new DragEvent('dragstart', { dataTransfer: dataTransfer }));
            arguments[1].dispatchEvent(new DragEvent('drop', { dataTransfer: dataTransfer }));
            arguments[0].dispatchEvent(new DragEvent('dragend', { dataTransfer: dataTransfer }));
        """, ingredient, constructor)
    
    @allure.step("Переключиться на секцию 'Соусы'")
    def go_to_sauces_section(self):
        """Перейти к секции соусов"""
        self.click_element(MainPageLocators.SAUCES_SECTION)
    
    @allure.step("Переключиться на секцию 'Начинки'")
    def go_to_fillings_section(self):
        """Перейти к секции начинок"""
        self.click_element(MainPageLocators.FILLINGS_SECTION)
    
    @allure.step("Получить активную секцию")
    def get_active_section(self):
        """Получить текст активной секции"""
        active_element = self.find_element(MainPageLocators.ACTIVE_SECTION)
        return active_element.text
    
    @allure.step("Открыть главную страницу")
    def open(self):
        """Открыть главную страницу"""
        self.driver.get(self.base_url)
        self.wait_for_page_load()
    
    @allure.step("Проверить что страница загружена")
    def is_page_loaded(self):
        """Проверить загрузку страницы"""
        return self.is_element_visible(MainPageLocators.PAGE_TITLE)
    
    @allure.step("Оформить заказ")
    def make_order(self):
        """Нажать кнопку оформления заказа"""
        self.click_element(MainPageLocators.ORDER_BUTTON)