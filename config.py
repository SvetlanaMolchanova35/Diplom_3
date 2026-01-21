class TestData:
    BASE_URL = "https://stellarburgers.education-services.ru"
    API_URL = f"{BASE_URL}/api"
    
    # Время ожидания
    DEFAULT_TIMEOUT = 10
    
    # ID ингредиентов (получены через API)
    INGREDIENTS = {
        "bun": "61c0c5a71d1f82001bdaaa6d",  # Флюоресцентная булка R2-D3
        "sauce": "61c0c5a71d1f82001bdaaa72",  # Соус Spicy-X
        "main": "61c0c5a71d1f82001bdaaa70"   # Говяжий метеорит
    }