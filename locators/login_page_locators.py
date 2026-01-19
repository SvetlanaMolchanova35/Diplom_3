from selenium.webdriver.common.by import By


class LoginPageLocators:
    # Форма входа
    EMAIL_INPUT = (By.XPATH, "//input[@type='text' and @name='name']")
    PASSWORD_INPUT = (By.XPATH, "//input[@type='password' and @name='Пароль']")
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти' and @type='submit']")
    
    # Ссылки
    REGISTER_LINK = (By.XPATH, "//a[text()='Зарегистрироваться']")
    FORGOT_PASSWORD_LINK = (By.XPATH, "//a[text()='Восстановить пароль']")
    
    # Заголовок
    LOGIN_TITLE = (By.XPATH, "//h2[text()='Вход']")
    
    # Форма регистрации
    REG_NAME_INPUT = (By.XPATH, "//input[@name='name']")
    REG_EMAIL_INPUT = (By.XPATH, "//input[@name='name' and @type='text']")
    REG_PASSWORD_INPUT = (By.XPATH, "//input[@type='password']")
    REGISTER_BUTTON = (By.XPATH, "//button[text()='Зарегистрироваться']")
    
    # Уведомления
    ERROR_MESSAGE = (By.XPATH, "//p[contains(@class, 'input__error')]")
    SUCCESS_MESSAGE = (By.XPATH, "//p[contains(@class, 'success')]")