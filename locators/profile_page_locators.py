from selenium.webdriver.common.by import By


class ProfilePageLocators:
    # Навигация в личном кабинете
    PROFILE_TAB = (By.XPATH, "//a[text()='Профиль']")
    ORDER_HISTORY_TAB = (By.XPATH, "//a[text()='История заказов']")
    LOGOUT_BUTTON = (By.XPATH, "//button[text()='Выход']")
    
    # Форма редактирования профиля
    NAME_INPUT = (By.XPATH, "//input[@name='name' and @value]")
    EMAIL_INPUT = (By.XPATH, "//input[@name='name' and contains(@type, 'text')]")
    PASSWORD_INPUT = (By.XPATH, "//input[@type='password']")
    SAVE_BUTTON = (By.XPATH, "//button[text()='Сохранить']")
    CANCEL_BUTTON = (By.XPATH, "//button[text()='Отмена']")
    
    # История заказов
    ORDER_HISTORY_LIST = (By.XPATH, "//div[contains(@class, 'OrderHistory_list__')]")
    ORDER_HISTORY_ITEMS = (By.XPATH, "//div[contains(@class, 'OrderHistory_listItem__')]")
    
    # Конструктор и лента заказов из профиля
    CONSTRUCTOR_LINK = (By.XPATH, "//p[text()='Конструктор']/parent::a")
    ORDER_FEED_LINK = (By.XPATH, "//p[text()='Лента заказов']/parent::a")
    
    # Заголовок
    PROFILE_TITLE = (By.XPATH, "//h2[contains(text(), 'В этом разделе вы можете')]")