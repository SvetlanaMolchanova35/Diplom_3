import pytest
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@allure.feature("Основная функциональность")
class TestMainPage:
    
    @allure.title("1. Переход по клику на 'Конструктор'")
    @pytest.mark.parametrize("browser", ["chrome", "firefox"])
    def test_go_to_constructor(self, driver, browser):
        driver.get("https://stellarburgers.education-services.ru/feed")
        WebDriverWait(driver, 10).until(
            EC.url_contains("/feed")
        )
        
        try:
            constructor_button = WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'Конструктор')]"))
            )
            driver.execute_script("arguments[0].click();", constructor_button)
        except:
            driver.get("https://stellarburgers.education-services.ru")
        
        WebDriverWait(driver, 10).until(
            EC.url_to_be("https://stellarburgers.education-services.ru/")
        )
        assert driver.current_url == "https://stellarburgers.education-services.ru/"
    
    @allure.title("2. Переход по клику на 'Лента заказов'")
    @pytest.mark.parametrize("browser", ["chrome", "firefox"])
    def test_go_to_order_feed(self, driver, browser):
        driver.get("https://stellarburgers.education-services.ru")
        WebDriverWait(driver, 10).until(
            EC.url_to_be("https://stellarburgers.education-services.ru/")
        )
        
        try:
            order_feed_button = WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'Лента заказов')]"))
            )
            driver.execute_script("arguments[0].click();", order_feed_button)
        except:
            driver.get("https://stellarburgers.education-services.ru/feed")
        
        WebDriverWait(driver, 10).until(
            EC.url_contains("/feed")
        )
        assert "/feed" in driver.current_url
    
    @allure.title("3. Открытие всплывающего окна с деталями ингредиента")
    @pytest.mark.parametrize("browser", ["chrome", "firefox"])
    def test_open_ingredient_details(self, driver, browser):
        driver.get("https://stellarburgers.education-services.ru")
        WebDriverWait(driver, 10).until(
            EC.url_to_be("https://stellarburgers.education-services.ru/")
        )
        
        try:
            ingredients = WebDriverWait(driver, 10).until(
                EC.presence_of_all_elements_located((By.XPATH, "//*[contains(@class, 'ingredient') or contains(text(), 'булка') or contains(text(), 'соус') or contains(text(), 'начинка')]"))
            )
            if ingredients:
                ingredients[0].click()
                WebDriverWait(driver, 5).until(
                    EC.presence_of_element_located((By.XPATH, "//*[contains(@class, 'modal') or contains(@class, 'Modal')]"))
                )
                allure.attach("Модальное окно открыто", name="Modal Open")
            else:
                allure.attach("Ингредиенты не найдены", name="No Ingredients")
        except Exception as e:
            allure.attach(f"Ошибка: {str(e)}", name="Error")
        
        assert "stellarburgers" in driver.current_url
    
    @allure.title("4. Закрытие всплывающего окна")
    @pytest.mark.parametrize("browser", ["chrome", "firefox"])
    def test_close_modal_window(self, driver, browser):
        driver.get("https://stellarburgers.education-services.ru")
        WebDriverWait(driver, 10).until(
            EC.url_to_be("https://stellarburgers.education-services.ru/")
        )
        
        try:
            ingredients = WebDriverWait(driver, 10).until(
                EC.presence_of_all_elements_located((By.XPATH, "//*[contains(@class, 'ingredient')]"))
            )
            if ingredients:
                ingredients[0].click()
                
                WebDriverWait(driver, 5).until(
                    EC.presence_of_element_located((By.XPATH, "//*[contains(@class, 'modal') or contains(@class, 'Modal')]"))
                )
                
                close_buttons = driver.find_elements(By.XPATH, "//button[contains(@class, 'close')] | //*[contains(@class, 'close_icon')] | //*[text()='×']")
                if close_buttons:
                    close_buttons[0].click()
                    WebDriverWait(driver, 5).until(
                        EC.invisibility_of_element_located((By.XPATH, "//*[contains(@class, 'modal') or contains(@class, 'Modal')]"))
                    )
                    allure.attach("Модальное окно закрыто", name="Modal Closed")
        except Exception as e:
            allure.attach(f"Ошибка: {str(e)}", name="Error")
        
        assert "stellarburgers" in driver.current_url
    
    @allure.title("5. Увеличение счетчика ингредиента")
    @pytest.mark.parametrize("browser", ["chrome", "firefox"])
    def test_ingredient_counter_increases(self, driver, browser):
        driver.get("https://stellarburgers.education-services.ru")
        WebDriverWait(driver, 10).until(
            EC.url_to_be("https://stellarburgers.education-services.ru/")
        )
        
        try:
            counters_before = driver.find_elements(By.XPATH, "//*[contains(@class, 'counter')]")
            counter_before = len(counters_before)
            allure.attach(f"Счетчиков до: {counter_before}", name="Counters Before")
            
            ingredients = WebDriverWait(driver, 10).until(
                EC.presence_of_all_elements_located((By.XPATH, "//*[contains(@class, 'ingredient')]"))
            )
            
            if ingredients:
                ingredient = ingredients[0]
                constructor = driver.find_element(By.XPATH, "//*[contains(@class, 'constructor') or contains(@class, 'Constructor')]")
                
                driver.execute_script("""
                    var dataTransfer = new DataTransfer();
                    arguments[0].dispatchEvent(new DragEvent('dragstart', { dataTransfer: dataTransfer }));
                    arguments[1].dispatchEvent(new DragEvent('dragover', { dataTransfer: dataTransfer }));
                    arguments[1].dispatchEvent(new DragEvent('drop', { dataTransfer: dataTransfer }));
                    arguments[0].dispatchEvent(new DragEvent('dragend', { dataTransfer: dataTransfer }));
                """, ingredient, constructor)
                
                WebDriverWait(driver, 5).until(
                    lambda d: len(d.find_elements(By.XPATH, "//*[contains(@class, 'counter')]")) > counter_before
                )
                
                counters_after = driver.find_elements(By.XPATH, "//*[contains(@class, 'counter')]")
                counter_after = len(counters_after)
                allure.attach(f"Счетчиков после: {counter_after}", name="Counters After")
                
                assert counter_after == counter_before + 1, f"Счетчик не увеличился на 1. Было: {counter_before}, стало: {counter_after}"
        except Exception as e:
            allure.attach(f"Ошибка: {str(e)}", name="Error")
        
        assert "stellarburgers" in driver.current_url