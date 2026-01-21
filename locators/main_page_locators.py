from selenium.webdriver.common.by import By


class MainPageLocators:
    # Основные кнопки навигации
    CONSTRUCTOR_BUTTON = (By.XPATH, "//a[contains(@class, 'AppHeader_header__link')]/p[text()='Конструктор']")
    ORDER_FEED_BUTTON = (By.XPATH, "//a[contains(@class, 'AppHeader_header__link')]/p[text()='Лента заказов']")
    PERSONAL_ACCOUNT_BUTTON = (By.XPATH, "//a[contains(@class, 'AppHeader_header__link')]/p[text()='Личный Кабинет']")
    
    # Секции конструктора
    BUNS_SECTION = (By.XPATH, "//span[text()='Булки']/parent::div")
    SAUCES_SECTION = (By.XPATH, "//span[text()='Соусы']/parent::div")
    FILLINGS_SECTION = (By.XPATH, "//span[text()='Начинки']/parent::div")
    
    # Ингредиенты
    INGREDIENT_ITEM = (By.XPATH, "//a[contains(@class, 'BurgerIngredient_ingredient')]")
    INGREDIENT_COUNTER = (By.XPATH, "//div[contains(@class, 'counter')]")
    
    # Модальное окно
    MODAL_OVERLAY = (By.XPATH, "//div[contains(@class, 'Modal_modal_overlay')]")
    MODAL_CONTENT = (By.XPATH, "//div[contains(@class, 'Modal_modal_content')]")
    MODAL_CLOSE_BUTTON = (By.XPATH, "//button[contains(@class, 'Modal_modal_close')]")
    
    # Детали ингредиента в модальном окне
    INGREDIENT_DETAILS_NAME = (By.XPATH, "//div[contains(@class, 'Modal_modal_header')]/h2")
    
    # Конструктор
    CONSTRUCTOR_AREA = (By.XPATH, "//section[contains(@class, 'BurgerConstructor_constructor_list')]")
    ORDER_BUTTON = (By.XPATH, "//button[contains(text(), 'Оформить заказ')]")
    
    # Заголовок страницы
    PAGE_TITLE = (By.XPATH, "//h1[text()='Соберите бургер']")
    
    # Локаторы для проверки URL
    CONSTRUCTOR_PAGE = (By.XPATH, "//h1[contains(text(), 'бургер')]")
    ORDER_FEED_PAGE = (By.XPATH, "//h1[contains(text(), 'Лента заказов')]")