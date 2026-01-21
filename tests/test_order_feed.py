import pytest
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from helpers.api_client import ApiClient


@allure.feature("Лента заказов")
class TestOrderFeed:
    
    @allure.title("6. Проверка увеличения счетчика 'Выполнено за все время'")
    @pytest.mark.parametrize("browser", ["chrome", "firefox"])
    def test_total_orders_counter_increases(self, authorized_driver, browser, test_user):
        driver = authorized_driver
        api_client = ApiClient()
        
        driver.get("https://stellarburgers.education-services.ru/feed")
        WebDriverWait(driver, 10).until(
            EC.url_contains("/feed")
        )
        
        total_elements = driver.find_elements(By.XPATH, "//*[contains(text(), 'все время') or contains(text(), 'всё время')]/following-sibling::*")
        assert len(total_elements) > 0, "Элемент счетчика 'Все время' не найден"
        
        total_text = total_elements[0].text
        assert total_text.isdigit(), f"Текст счетчика не является числом: {total_text}"
        total_before = int(total_text)
        
        allure.attach(f"Счетчик до: {total_before}", name="Total Before")
        
        api_client.login(test_user["email"], test_user["password"])
        
        ingredients = ["61c0c5a71d1f82001bdaaa6d", "61c0c5a71d1f82001bdaaa72"]
        order_response = api_client.create_order(ingredients)
        
        assert order_response.get("success"), f"Не удалось создать заказ: {order_response}"
        order_number = order_response.get("order", {}).get("number")
        allure.attach(f"Создан заказ №{order_number}", name="Order Created")
        
        WebDriverWait(driver, 10).until(
            lambda d: api_client.get_all_orders().get("total", 0) > 0
        )
        
        driver.refresh()
        WebDriverWait(driver, 10).until(
            EC.url_contains("/feed")
        )
        
        total_elements_after = driver.find_elements(By.XPATH, "//*[contains(text(), 'все время') or contains(text(), 'всё время')]/following-sibling::*")
        assert len(total_elements_after) > 0, "Элемент счетчика 'Все время' не найден после обновления"
        
        total_text_after = total_elements_after[0].text
        assert total_text_after.isdigit(), f"Текст счетчика не является числом: {total_text_after}"
        total_after = int(total_text_after)
        
        allure.attach(f"Счетчик после: {total_after}", name="Total After")
        
        assert total_after == total_before + 1, f"Счетчик не увеличился на 1. Было: {total_before}, стало: {total_after}"
    
    @allure.title("7. Проверка увеличения счетчика 'Выполнено за сегодня'")
    @pytest.mark.parametrize("browser", ["chrome", "firefox"])
    def test_today_orders_counter_increases(self, authorized_driver, browser, test_user):
        driver = authorized_driver
        api_client = ApiClient()
        
        driver.get("https://stellarburgers.education-services.ru/feed")
        WebDriverWait(driver, 10).until(
            EC.url_contains("/feed")
        )
        
        today_elements = driver.find_elements(By.XPATH, "//*[contains(text(), 'сегодня') or contains(text(), 'Сегодня')]/following-sibling::*")
        assert len(today_elements) > 0, "Элемент счетчика 'Сегодня' не найден"
        
        today_text = today_elements[0].text
        assert today_text.isdigit(), f"Текст счетчика не является числом: {today_text}"
        today_before = int(today_text)
        
        allure.attach(f"Счетчик сегодня до: {today_before}", name="Today Before")
        
        api_client.login(test_user["email"], test_user["password"])
        
        ingredients = ["61c0c5a71d1f82001bdaaa6d", "61c0c5a71d1f82001bdaaa70"]
        order_response = api_client.create_order(ingredients)
        
        assert order_response.get("success"), f"Не удалось создать заказ: {order_response}"
        
        WebDriverWait(driver, 10).until(
            lambda d: api_client.get_all_orders().get("totalToday", 0) > 0
        )
        
        driver.refresh()
        WebDriverWait(driver, 10).until(
            EC.url_contains("/feed")
        )
        
        today_elements_after = driver.find_elements(By.XPATH, "//*[contains(text(), 'сегодня') or contains(text(), 'Сегодня')]/following-sibling::*")
        assert len(today_elements_after) > 0, "Элемент счетчика 'Сегодня' не найден после обновления"
        
        today_text_after = today_elements_after[0].text
        assert today_text_after.isdigit(), f"Текст счетчика не является числом: {today_text_after}"
        today_after = int(today_text_after)
        
        allure.attach(f"Счетчик сегодня после: {today_after}", name="Today After")
        
        assert today_after == today_before + 1, f"Счетчик 'Сегодня' не увеличился на 1. Было: {today_before}, стало: {today_after}"
    
    @allure.title("8. Проверка появления заказа в разделе 'В работе'")
    @pytest.mark.parametrize("browser", ["chrome", "firefox"])
    def test_order_appears_in_progress(self, authorized_driver, browser, test_user):
        driver = authorized_driver
        api_client = ApiClient()
        
        api_client.login(test_user["email"], test_user["password"])
        
        ingredients = ["61c0c5a71d1f82001bdaaa6d", "61c0c5a71d1f82001bdaaa72", "61c0c5a71d1f82001bdaaa70"]
        order_response = api_client.create_order(ingredients)
        
        assert order_response.get("success"), f"Не удалось создать заказ: {order_response}"
        order_number = order_response.get("order", {}).get("number")
        allure.attach(f"Создан заказ №{order_number}", name="Order Number")
        
        driver.get("https://stellarburgers.education-services.ru/feed")
        WebDriverWait(driver, 10).until(
            EC.url_contains("/feed")
        )
        
        order_elements = driver.find_elements(By.XPATH, f"//*[contains(text(), '{order_number}')]")
        
        assert len(order_elements) > 0, f"Заказ №{order_number} не найден в разделе 'В работе'"
        allure.attach(f"Заказ №{order_number} найден в разделе 'В работе'", name="Order Found")