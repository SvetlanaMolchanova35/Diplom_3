from pages.base_page import BasePage
from locators.login_page_locators import LoginPageLocators
import allure


class LoginPage(BasePage):
    
    @allure.step("Открыть страницу входа")
    def open(self):
        self.driver.get(f"{self.base_url}/login")
        self.wait_for_page_load()
    
    @allure.step("Войти с email '{email}' и паролем '{password}'")
    def login(self, email, password):
        self.send_keys(LoginPageLocators.EMAIL_INPUT, email)
        self.send_keys(LoginPageLocators.PASSWORD_INPUT, password)
        self.click_element(LoginPageLocators.LOGIN_BUTTON)
        self.wait_for_page_load()
    
    @allure.step("Проверить что страница входа загружена")
    def is_login_page_loaded(self):
        return self.is_element_visible(LoginPageLocators.LOGIN_TITLE)
    
    @allure.step("Перейти на страницу регистрации")
    def go_to_register_page(self):
        self.click_element(LoginPageLocators.REGISTER_LINK)
        self.wait_for_page_load()
    
    @allure.step("Проверить что отображается сообщение об ошибке")
    def is_error_message_displayed(self):
        return self.is_element_visible(LoginPageLocators.ERROR_MESSAGE, timeout=5)
    
    @allure.step("Получить текст ошибки")
    def get_error_text(self):
        return self.get_text(LoginPageLocators.ERROR_MESSAGE)