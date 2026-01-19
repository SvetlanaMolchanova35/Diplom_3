import allure
import time
import utils.urls as urls
from locators.user_profile_locators import AccountLocators, AccountPageHelper
from pages.base_page import BasePage


class AccountPage(BasePage):
    """
    Класс для работы со страницей личного кабинета
    """

    @allure.step("Проверка загрузки страницы личного кабинета")
    def is_account_page_loaded(self, timeout: int = 15) -> bool:
        """
        Проверяет, что страница личного кабинета загружена
        """
        for locator in AccountPageHelper.get_account_page_indicator():
            try:
                if self.is_element_present(locator, timeout=5):
                    print(f"DEBUG: Страница личного кабинета загружена (найден элемент по локатору)")
                    return True
            except:
                continue
        return False

    @allure.step("Найти ссылку 'История заказов'")
    def find_history_link(self, timeout: int = 15):
        """
        Ищет ссылку 'История заказов' разными способами
        """
        for locator in AccountPageHelper.get_all_history_locators():
            try:
                element = self.find_element_with_wait(locator, timeout=5)
                print(f"DEBUG: Найдена ссылка 'История заказов' по локатору")
                return element
            except:
                continue
        raise Exception("Не удалось найти ссылку 'История заказов'")

    @allure.step("Найти кнопку 'Выход'")
    def find_exit_button(self, timeout: int = 15):
        """
        Ищет кнопку 'Выход' разными способами
        """
        for locator in AccountPageHelper.get_all_exit_locators():
            try:
                element = self.find_element_with_wait(locator, timeout=5)
                print(f"DEBUG: Найдена кнопка 'Выход' по локатору")
                return element
            except:
                continue
        raise Exception("Не удалось найти кнопку 'Выход'")

    @allure.step("Клик на «История заказов»")
    def click_order_history_link(self) -> str:
        """
        Метод для перехода в раздел истории заказов
        :return: текущий URL после перехода
        """
        history_link = self.find_history_link()
        history_link.click()
        time.sleep(3)  # Даем время для перехода
        return self.get_current_url()

    @allure.step("Клик на кнопку «Выход»")
    def click_exit_button(self) -> str:
        """
        Метод для выхода из аккаунта
        :return: текущий URL после выхода
        """
        exit_button = self.find_exit_button()
        exit_button.click()
        time.sleep(3)  # Даем время для перехода
        return self.get_current_url()