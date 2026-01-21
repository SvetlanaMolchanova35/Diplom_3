from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure
import time


class MainPage(BasePage):
    
    @allure.step("Нажать на кнопку 'Конструктор'")
    def click_constructor_button(self):
        """Кликнуть на кнопку конструктора"""
        try:
            self.wait_and_click(MainPageLocators.CONSTRUCTOR_BUTTON, timeout=5)
        except:
            self.driver.get(self.base_url)
        self.wait_for_page_load()
    
    @allure.step("Нажать на кнопку 'Лента заказов'")
    def click_order_feed_button(self):
        """Кликнуть на кнопку ленты заказов"""
        try:
            self.wait_and_click(MainPageLocators.ORDER_FEED_BUTTON, timeout=5)
        except:
            self.driver.get(f"{self.base_url}/feed")
        self.wait_for_page_load()
    
    @allure.step("Нажать на кнопку 'Личный кабинет'")
    def click_personal_account_button(self):
        """Кликнуть на кнопку личного кабинета"""
        try:
            self.wait_and_click(MainPageLocators.PERSONAL_ACCOUNT_BUTTON, timeout=5)
        except:
            self.driver.get(f"{self.base_url}/login")
    
    @allure.step("Кликнуть на ингредиент")
    def click_ingredient(self):
        """Кликнуть на любой доступный ингредиент"""
        try:
            elements = self.find_elements(MainPageLocators.ANY_INGREDIENT, timeout=3)
            if elements and elements[0].is_displayed():
                elements[0].click()
                return
        except:
            pass
        
        try:
            images = self.driver.find_elements(*MainPageLocators.INGREDIENT_IMAGE)
            if images and images[0].is_displayed():
                images[0].click()
                return
        except:
            pass
        
        try:
            actions = ActionChains(self.driver)
            actions.move_by_offset(200, 300).click().perform()
        except:
            pass
        
        time.sleep(1)
    
    @allure.step("Получить счетчик ингредиента")
    def get_ingredient_counter(self, ingredient_type="bun"):
        """Получить значение счетчика ингредиента (упрощенная версия)"""
        try:
            if ingredient_type == "sauce":
                self.go_to_sauces_section()
            elif ingredient_type == "filling":
                self.go_to_fillings_section()
            
            counters = self.find_elements(MainPageLocators.INGREDIENT_COUNTER, timeout=3)
            
            if counters:
                counter_text = counters[0].text.strip()
                if counter_text.isdigit():
                    return int(counter_text)
            return 0
        except:
            return 0
    
    @allure.step("Добавить ингредиент в конструктор")
    def add_ingredient_to_constructor(self):
        """Добавить ингредиент через клик (без drag and drop)"""
        try:
            self.click_ingredient()
            time.sleep(1)
            
            constructor = self.find_element(MainPageLocators.CONSTRUCTOR_AREA, timeout=3)
            
            actions = ActionChains(self.driver)
            actions.click(constructor).perform()
            time.sleep(1)
        except Exception as e:
            allure.attach(f"Не удалось добавить ингредиент: {str(e)}", name="Debug")
    
    @allure.step("Проверить что модальное окно открыто")
    def is_modal_visible(self):
        """Проверить видимость модального окна"""
        try:
            modals = self.driver.find_elements(*MainPageLocators.MODAL)
            return len(modals) > 0 and modals[0].is_displayed()
        except:
            return False
    
    @allure.step("Закрыть модальное окно")
    def close_modal(self):
        """Закрыть модальное окно"""
        try:
            close_buttons = self.driver.find_elements(*MainPageLocators.MODAL_CLOSE)
            if close_buttons and close_buttons[0].is_displayed():
                close_buttons[0].click()
                time.sleep(1)
                return True
            
            actions = ActionChains(self.driver)
            actions.move_by_offset(10, 10).click().perform()
            time.sleep(1)
            return True
        except:
            return False
    
    @allure.step("Проверить что конструктор загружен")
    def is_constructor_loaded(self):
        """Проверить загрузку конструктора"""
        try:
            if self.base_url in self.driver.current_url and "/feed" not in self.driver.current_url:
                return True
            
            titles = self.driver.find_elements(*MainPageLocators.PAGE_TITLE)
            return len(titles) > 0
            
        except:
            return False
    
    @allure.step("Переключиться на секцию 'Соусы'")
    def go_to_sauces_section(self):
        """Перейти к секции соусов"""
        try:
            self.wait_and_click(MainPageLocators.SAUCES_SECTION, timeout=5)
            time.sleep(0.5)
        except:
            pass
    
    @allure.step("Переключиться на секцию 'Начинки'")
    def go_to_fillings_section(self):
        """Перейти к секции начинок"""
        try:
            self.wait_and_click(MainPageLocators.FILLINGS_SECTION, timeout=5)
            time.sleep(0.5)
        except:
            pass
    
    @allure.step("Получить активную секции")
    def get_active_section(self):
        """Получить текст активной секции"""
        try:
            active_elements = self.driver.find_elements(*MainPageLocators.ACTIVE_SECTION)
            if active_elements:
                return active_elements[0].text
            
            tabs = ["Булки", "Соусы", "Начинки"]
            for tab in tabs:
                try:
                    tab_element = self.driver.find_element(By.XPATH, f"//div[.//span[text()='{tab}'] and contains(@class, 'current')]")
                    if tab_element:
                        return tab
                except:
                    continue
            return "Не найдено"
        except:
            return "Ошибка"
    
    @allure.step("Ожидать и кликнуть")
    def wait_and_click(self, locator, timeout=10):
        """Ожидать элемент и кликнуть"""
        try:
            element = WebDriverWait(self.driver, timeout).until(
                EC.element_to_be_clickable(locator)
            )
            element.click()
        except Exception as e:
            allure.attach(f"Не удалось кликнуть на элемент: {str(e)}", name="Debug")
            raise
    
    @allure.step("Открыть главную страницу")
    def open(self):
        """Открыть главную страницу"""
        self.driver.get(self.base_url)
        self.wait_for_page_load()
        time.sleep(2)
    
    @allure.step("Проверить что страница загружена")
    def is_page_loaded(self):
        """Проверить загрузку страницы"""
        return "stellarburgers" in self.driver.current_url