from pages.base_page import BasePage
from locators.order_feed_locators import OrderFeedLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure
import re


class OrderFeedPage(BasePage):
    
    @allure.step("Открыть ленту заказов")
    def open(self):
        self.driver.get(f"{self.base_url}/feed")
        self.wait_for_page_load()
        self.wait_for_visibility(OrderFeedLocators.ORDER_FEED_TITLE)
    
    @allure.step("Получить общее количество заказов")
    def get_total_orders_count(self):
        try:
            text = self.get_text(OrderFeedLocators.TOTAL_ORDERS_COUNT)
            # Извлекаем только цифры из текста
            numbers = re.findall(r'\d+', text)
            return int(numbers[0]) if numbers else 0
        except:
            return 0
    
    @allure.step("Получить количество заказов за сегодня")
    def get_today_orders_count(self):
        try:
            text = self.get_text(OrderFeedLocators.TODAY_ORDERS_COUNT)
            numbers = re.findall(r'\d+', text)
            return int(numbers[0]) if numbers else 0
        except:
            return 0
    
    @allure.step("Получить количество заказов в работе")
    def get_orders_in_progress_count(self):
        elements = self.find_elements(OrderFeedLocators.ORDERS_IN_PROGRESS, timeout=5)
        return len(elements)
    
    @allure.step("Кликнуть на первый заказ в ленте")
    def click_first_order(self):
        self.wait_and_click(OrderFeedLocators.FIRST_ORDER_CARD)
    
    @allure.step("Проверить что открыто модальное окно деталей заказа")
    def is_order_details_modal_open(self):
        return self.is_element_visible(OrderFeedLocators.ORDER_DETAILS_MODAL)
    
    @allure.step("Получить номер заказа из модального окна")
    def get_order_number_from_modal(self):
        text = self.get_text(OrderFeedLocators.ORDER_NUMBER_IN_MODAL)
        numbers = re.findall(r'\d+', text)
        return numbers[0] if numbers else None
    
    @allure.step("Перейти в конструктор из ленты заказов")
    def go_to_constructor_from_feed(self):
        self.wait_and_click(OrderFeedLocators.CONSTRUCTOR_LINK_IN_FEED)
        self.wait_for_page_load()
    
    @allure.step("Обновить ленту заказов")
    def refresh_feed(self):
        self.driver.refresh()
        self.wait_for_visibility(OrderFeedLocators.ORDER_FEED_TITLE)
    
    @allure.step("Проверить что лента заказов загружена")
    def is_feed_loaded(self):
        return self.is_element_visible(OrderFeedLocators.ORDER_FEED_TITLE)
    
    @allure.step("Ожидать и кликнуть")
    def wait_and_click(self, locator, timeout=10):
        element = WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator)
        )
        element.click()