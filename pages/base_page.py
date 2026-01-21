from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
import allure


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.base_url = "https://stellarburgers.education-services.ru"
    
    @allure.step("Открыть страницу")
    def open(self, url=""):
        if url.startswith("http"):
            full_url = url
        else:
            full_url = f"{self.base_url}{url}"
        
        self.driver.get(full_url)
        self.wait_for_page_load()
    
    @allure.step("Найти элемент")
    def find_element(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located(locator),
            message=f"Не удалось найти элемент по локатору {locator}"
        )
    
    @allure.step("Найти элементы")
    def find_elements(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_all_elements_located(locator),
            message=f"Не удалось найти элементы по локатору {locator}"
        )
    
    @allure.step("Кликнуть по элементу")
    def click_element(self, locator):
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(locator)
        )
        element.click()
    
    @allure.step("Ввести текст '{text}'")
    def send_keys(self, locator, text):
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)
    
    @allure.step("Получить текст элемента")
    def get_text(self, locator):
        return self.find_element(locator).text
    
    @allure.step("Получить атрибут элемента")
    def get_attribute(self, locator, attribute):
        element = self.find_element(locator)
        return element.get_attribute(attribute)
    
    @allure.step("Ожидать видимости элемента")
    def wait_for_visibility(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )
    
    @allure.step("Ожидать исчезновения элемента")
    def wait_for_invisibility(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.invisibility_of_element_located(locator)
        )
    
    @allure.step("Ожидать кликабельности элемента")
    def wait_for_clickable(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator)
        )
    
    @allure.step("Проверить, что элемент видим")
    def is_element_visible(self, locator, timeout=5):
        try:
            self.wait_for_visibility(locator, timeout)
            return True
        except:
            return False
    
    @allure.step("Проверить, что элемент существует")
    def is_element_present(self, locator, timeout=5):
        try:
            self.find_element(locator, timeout)
            return True
        except:
            return False
    
    @allure.step("Перетащить и отпустить элемент")
    def drag_and_drop(self, source_locator, target_locator):
        source = self.find_element(source_locator)
        target = self.find_element(target_locator)
        actions = ActionChains(self.driver)
        actions.drag_and_drop(source, target).perform()
    
    @allure.step("Сделать скриншот")
    def take_screenshot(self, filename="screenshot.png"):
        self.driver.save_screenshot(filename)
        allure.attach.file(filename, name="Screenshot", attachment_type=allure.attachment_type.PNG)
    
    @allure.step("Получить текущий URL")
    def get_current_url(self):
        return self.driver.current_url
    
    @allure.step("Получить заголовок страницы")
    def get_title(self):
        return self.driver.title
    
    @allure.step("Ожидать загрузки страницы")
    def wait_for_page_load(self, timeout=30):
        WebDriverWait(self.driver, timeout).until(
            lambda driver: driver.execute_script('return document.readyState') == 'complete'
        )
    
    @allure.step("Обновить страницу")
    def refresh_page(self):
        self.driver.refresh()
        self.wait_for_page_load()
    
    @allure.step("Вернуться на предыдущую страницу")
    def go_back(self):
        self.driver.back()
        self.wait_for_page_load()