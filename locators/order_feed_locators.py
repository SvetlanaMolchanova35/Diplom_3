from selenium.webdriver.common.by import By


class OrderFeedLocators:
    # Заголовок
    ORDER_FEED_TITLE = (By.XPATH, "//h1[text()='Лента заказов']")
    
    # Счетчики
    TOTAL_ORDERS_COUNT = (By.XPATH, "//p[text()='Выполнено за все время:']/following-sibling::p")
    TODAY_ORDERS_COUNT = (By.XPATH, "//p[text()='Выполнено за сегодня:']/following-sibling::p")
    
    # Заказы
    ORDER_CARDS = (By.CSS_SELECTOR, "[class*=OrderHistory_orderItem]")
    FIRST_ORDER_CARD = (By.CSS_SELECTOR, "[class*=OrderHistory_orderItem]:first-of-type")
    
    # Раздел "В работе"
    IN_PROGRESS_SECTION = (By.XPATH, "//ul[preceding-sibling::p[contains(text(), 'В работе')]]")
    ORDERS_IN_PROGRESS = (By.CSS_SELECTOR, "[class*=OrderFeed_orderNumber]")
    
    # Конструктор из ленты
    CONSTRUCTOR_LINK = (By.XPATH, "//p[text()='Конструктор']/parent::a")
    
    # Модальное окно деталей заказа
    ORDER_DETAILS_MODAL = (By.CSS_SELECTOR, "[class*=Modal_modal]")
    ORDER_NUMBER_IN_MODAL = (By.CSS_SELECTOR, "[class*=OrderDetails_title]")
    
    # Статистика
    ORDERS_STATS = (By.CSS_SELECTOR, "[class*=OrderFeed_orderStats]")