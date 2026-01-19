from selenium.webdriver.common.by import By


class OrderFeedLocators:
    # Заголовок
    ORDER_FEED_TITLE = (By.XPATH, "//h1[contains(text(), 'Лента') or contains(text(), 'Заказов')]")
    
    # Счетчики - простые локаторы
    TOTAL_ORDERS_COUNT = (By.XPATH, "//p[contains(text(), 'все время') or contains(text(), 'всё время')]/following-sibling::p")
    TODAY_ORDERS_COUNT = (By.XPATH, "//p[contains(text(), 'сегодня') or contains(text(), 'Сегодня')]/following-sibling::p")
    
    # Заказы
    ORDER_CARDS = (By.CSS_SELECTOR, "div[class*='order'], div[class*='Order']")
    FIRST_ORDER_CARD = (By.CSS_SELECTOR, "div[class*='order']:first-of-type, div[class*='Order']:first-of-type")
    
    # Раздел "В работе"
    IN_PROGRESS_SECTION = (By.XPATH, "//ul[.//p[contains(text(), 'Готовы') or contains(text(), 'готовы')]]")
    ORDERS_IN_PROGRESS = (By.CSS_SELECTOR, "ul li")
    
    # Конструктор из ленты
    CONSTRUCTOR_LINK = (By.XPATH, "//a[.//p[text()='Конструктор']]")