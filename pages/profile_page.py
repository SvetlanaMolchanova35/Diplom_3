from pages.base_page import BasePage
from locators.profile_page_locators import ProfilePageLocators
import allure


class ProfilePage(BasePage):
    
    @allure.step("Открыть страницу профиля")
    def open(self):
        self.driver.get(f"{self.base_url}/account/profile")
        self.wait_for_page_load()
    
    @allure.step("Перейти в раздел истории заказов")
    def go_to_order_history(self):
        self.click_element(ProfilePageLocators.ORDER_HISTORY_TAB)
        self.wait_for_page_load()
    
    @allure.step("Выйти из аккаунта")
    def logout(self):
        self.click_element(ProfilePageLocators.LOGOUT_BUTTON)
        self.wait_for_page_load()
    
    @allure.step("Проверить что профиль загружен")
    def is_profile_loaded(self):
        return self.is_element_visible(ProfilePageLocators.PROFILE_TITLE, timeout=10)
    
    @allure.step("Получить текущее имя из формы")
    def get_current_name(self):
        return self.get_attribute(ProfilePageLocators.NAME_INPUT, "value")
    
    @allure.step("Получить текущий email из формы")
    def get_current_email(self):
        return self.get_attribute(ProfilePageLocators.EMAIL_INPUT, "value")
    
    @allure.step("Обновить имя пользователя")
    def update_name(self, new_name):
        element = self.find_element(ProfilePageLocators.NAME_INPUT)
        element.clear()
        element.send_keys(new_name)
    
    @allure.step("Сохранить изменения")
    def save_changes(self):
        self.click_element(ProfilePageLocators.SAVE_BUTTON)
        self.wait_for_page_load()
    
    @allure.step("Перейти в конструктор из профиля")
    def go_to_constructor(self):
        self.click_element(ProfilePageLocators.CONSTRUCTOR_LINK)
        self.wait_for_page_load()
    
    @allure.step("Перейти в ленту заказов из профиля")
    def go_to_order_feed(self):
        self.click_element(ProfilePageLocators.ORDER_FEED_LINK)
        self.wait_for_page_load()
    
    @allure.step("Получить количество заказов в истории")
    def get_order_history_count(self):
        elements = self.find_elements(ProfilePageLocators.ORDER_HISTORY_ITEMS, timeout=5)
        return len(elements)