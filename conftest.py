import pytest
import allure
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from helpers.api_client import ApiClient


def pytest_addoption(parser):
    parser.addoption('--browser', action='store', default='chrome',
                     help="Choose browser: chrome or firefox")
    parser.addoption('--headless', action='store_true',
                     help="Run tests in headless mode")
    parser.addoption('--url', action='store', default='https://stellarburgers.education-services.ru',
                     help="Base URL for tests")


@pytest.fixture(scope="function")
def driver(request):
    browser = request.config.getoption("browser")
    headless = request.config.getoption("headless")
    base_url = request.config.getoption("url")
    
    if browser == "chrome":
        service = ChromeService(ChromeDriverManager().install())
        options = Options()
        if headless:
            options.add_argument("--headless")
        options.add_argument("--window-size=1920,1080")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--disable-gpu")
        options.add_argument("--disable-notifications")
        driver = webdriver.Chrome(service=service, options=options)
    elif browser == "firefox":
        service = FirefoxService(GeckoDriverManager().install())
        options = FirefoxOptions()
        if headless:
            options.add_argument("--headless")
        options.add_argument("--width=1920")
        options.add_argument("--height=1080")
        driver = webdriver.Firefox(service=service, options=options)
    else:
        raise pytest.UsageError("--browser should be chrome or firefox")
    
    driver.maximize_window()
    driver.base_url = base_url
    driver.implicitly_wait(10)
    
    yield driver
    
    # Закрываем браузер
    try:
        driver.quit()
    except:
        pass


@pytest.fixture(scope="session")
def api_client():
    """Фикстура для работы с API"""
    client = ApiClient()
    yield client


@pytest.fixture(scope="function")
def test_user(api_client):
    """Фикстура для тестового пользователя"""
    user = api_client.create_test_user()
    yield user
    
    # Удаляем тестового пользователя после теста
    api_client.delete_test_user()


@pytest.fixture(scope="function")
def authorized_driver(driver, test_user):
    """Фикстура для авторизованного драйвера"""
    from pages.login_page import LoginPage
    
    # Авторизуемся через API для надежности
    api_client = ApiClient()
    api_client.login(test_user["email"], test_user["password"])
    
    # Открываем главную страницу
    driver.get("https://stellarburgers.education-services.ru")
    
    # Добавляем токен в куки для авторизации
    if api_client.token:
        driver.add_cookie({
            'name': 'accessToken',
            'value': api_client.token.replace('Bearer ', ''),
            'domain': 'stellarburgers.education-services.ru'
        })
        driver.refresh()
    
    yield driver


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Хук для создания скриншотов при падении тестов"""
    outcome = yield
    rep = outcome.get_result()
    
    if rep.when == "call" and rep.failed:
        try:
            if "driver" in item.fixturenames:
                driver = item.funcargs["driver"]
                
                import datetime
                timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
                test_name = item.name.replace("[", "_").replace("]", "_").replace(":", "_")
                screenshot_name = f"screenshots/failure_{test_name}_{timestamp}.png"
                
                driver.save_screenshot(screenshot_name)
                
                allure.attach.file(screenshot_name, 
                                 name="Failure Screenshot",
                                 attachment_type=allure.attachment_type.PNG)
        except Exception as e:
            print(f"Не удалось создать скриншот: {e}")


def pytest_configure(config):
    """Конфигурация pytest"""
    config.addinivalue_line("markers", "smoke: smoke tests")
    config.addinivalue_line("markers", "regression: regression tests")
    config.addinivalue_line("markers", "ui: ui tests")
    config.addinivalue_line("markers", "api: api tests")
    config.addinivalue_line("markers", "chrome: tests for chrome browser")
    config.addinivalue_line("markers", "firefox: tests for firefox browser")