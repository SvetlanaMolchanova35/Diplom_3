from selenium.webdriver.common.by import By


class MainPageLocators:
    # Основные кнопки навигации - простые локаторы
    CONSTRUCTOR_BUTTON = (By.XPATH, "//a[.//p[text()='Конструктор']]")
    ORDER_FEED_BUTTON = (By.XPATH, "//a[.//p[text()='Лента Заказов']]")
    PERSONAL_ACCOUNT_BUTTON = (By.XPATH, "//a[.//p[text()='Личный Кабинет']]")
    
    # Секции конструктора - по тексту
    BUNS_SECTION = (By.XPATH, "//div[.//span[text()='Булки']]")
    SAUCES_SECTION = (By.XPATH, "//div[.//span[text()='Соусы']]")
    FILLINGS_SECTION = (By.XPATH, "//div[.//span[text()='Начинки']]")
    
    # Активная секция
    ACTIVE_SECTION = (By.CSS_SELECTOR, "div[class*='current']")
    
    # Ингредиенты - простые селекторы
    ANY_INGREDIENT = (By.CSS_SELECTOR, "a[href*='ingredient'], div[class*='ingredient'], div[class*='Ingredient']")
    INGREDIENT_IMAGE = (By.CSS_SELECTOR, "img[alt*='ингредиент'], img[src*='ingredient']")
    
    # Счетчики
    INGREDIENT_COUNTER = (By.CSS_SELECTOR, "div[class*='counter']")
    
    # Конструктор
    CONSTRUCTOR_AREA = (By.CSS_SELECTOR, "section[class*='constructor'], section[class*='Constructor']")
    
    # Кнопка оформления
    ORDER_BUTTON = (By.XPATH, "//button[contains(text(), 'Оформить') or contains(text(), 'оформить')]")
    
    # Модальные окна
    MODAL = (By.CSS_SELECTOR, "div[class*='modal'], div[class*='Modal']")
    MODAL_CLOSE = (By.CSS_SELECTOR, "button[class*='close'], svg[class*='close']")
    
    # Детали в модальном окне
    MODAL_TITLE = (By.CSS_SELECTOR, "h2, h3")
    MODAL_DETAILS = (By.XPATH, "//li[contains(text(), 'калории') or contains(text(), 'Калории')]")
    
    # Заголовок страницы
    PAGE_TITLE = (By.XPATH, "//h1[contains(text(), 'Соберите') or contains(text(), 'бургер')]")