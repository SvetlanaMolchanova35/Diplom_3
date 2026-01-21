from pages.base_page import BasePage
from locators.order_feed_locators import OrderFeedLocators
import allure


class OrderFeedPage(BasePage):
    
    @allure.step("Открыть ленту заказов")
    def open(self):
        self.driver.get(f"{self.base_url}/feed")
        self.wait_for_visibility(OrderFeedLocators.ORDER_FEED_TITLE)
    
    @allure.step("Получить общее количество заказов")
    def get_total_orders_count(self):
        text = self.get_text(OrderFeedLocators.TOTAL_ORDERS_COUNT)
        return int(text) if text.isdigit() else 0
    
    @allure.step("Получить количество заказов за сегодня")
    def get_today_orders_count(self):
        text = self.get_text(OrderFeedLocators.TODAY_ORDERS_COUNT)
        return int(text) if text.isdigit() else 0
    
    @allure.step("Получить список номеров заказов в работе")
    def get_orders_in_progress_numbers(self):
        """Получить список номеров заказов в разделе 'В работе'"""
        if self.is_element_present(OrderFeedLocators.ORDERS_IN_PROGRESS):
            elements = self.find_elements(OrderFeedLocators.ORDERS_IN_PROGRESS)
            return [int(elem.text) for elem in elements if elem.text.isdigit()]
        return []
    
    @allure.step("Кликнуть на первый заказ в ленте")
    def click_first_order(self):
        self.click_element(OrderFeedLocators.FIRST_ORDER_CARD)
    
    @allure.step("Проверить что открыто модальное окно деталей заказа")
    def is_order_details_modal_open(self):
        return self.is_element_visible(OrderFeedLocators.ORDER_DETAILS_MODAL)
    
    @allure.step("Перейти в конструктор из ленты заказов")
    def go_to_constructor_from_feed(self):
        self.click_element(OrderFeedLocators.CONSTRUCTOR_LINK)
        self.wait_for_page_load()
    
    @allure.step("Обновить ленту заказов")
    def refresh_feed(self):
        self.driver.refresh()
        self.wait_for_visibility(OrderFeedLocators.ORDER_FEED_TITLE)
    
    @allure.step("Проверить что лента заказов загружена")
    def is_feed_loaded(self):
        return self.is_element_visible(OrderFeedLocators.ORDER_FEED_TITLE)
    
    @allure.step("Проверить что номер заказа есть в разделе 'В работе'")
    def is_order_in_progress(self, order_number):
        """Проверить что указанный номер заказа есть в разделе 'В работе'"""
        orders_in_progress = self.get_orders_in_progress_numbers()
        return order_number in orders_in_progress