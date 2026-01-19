import requests
import allure
import time
import random


class ApiClient:
    def __init__(self, base_url="https://stellarburgers.education-services.ru/api"):
        self.base_url = base_url
        self.token = None
    
    @allure.step("Создать тестового пользователя")
    def create_test_user(self):
        """Создание уникального тестового пользователя"""
        timestamp = int(time.time())
        random_num = random.randint(1000, 9999)
        email = f"test_user_{timestamp}_{random_num}@example.com"
        password = "TestPassword123"
        name = f"Test User {timestamp}"
        
        data = {
            "email": email,
            "password": password,
            "name": name
        }
        
        response = requests.post(f"{self.base_url}/auth/register", json=data, timeout=10)
        
        if response.status_code == 200:
            user_data = response.json()
            self.token = user_data.get("accessToken")
            allure.attach(f"Создан пользователь: {email}", name="User Created")
            return {
                "email": email,
                "password": password,
                "name": name,
                "access_token": self.token
            }
        else:
            # Если пользователь уже существует, пробуем авторизоваться
            try:
                login_data = {"email": email, "password": password}
                response = requests.post(f"{self.base_url}/auth/login", json=login_data, timeout=10)
                if response.status_code == 200:
                    user_data = response.json()
                    self.token = user_data.get("accessToken")
                    allure.attach(f"Авторизован существующий пользователь: {email}", name="User Logged In")
                    return {
                        "email": email,
                        "password": password,
                        "name": name,
                        "access_token": self.token
                    }
            except Exception as e:
                pass
            
            # Если не получилось, создаем с другим email
            email = f"test_user_{timestamp}_{random_num}_alt@example.com"
            data["email"] = email
            
            response = requests.post(f"{self.base_url}/auth/register", json=data, timeout=10)
            if response.status_code == 200:
                user_data = response.json()
                self.token = user_data.get("accessToken")
                allure.attach(f"Создан пользователь (альтернативный email): {email}", name="User Created Alt")
                return {
                    "email": email,
                    "password": password,
                    "name": name,
                    "access_token": self.token
                }
            
            raise Exception(f"Не удалось создать/авторизовать пользователя. Код: {response.status_code}, Ответ: {response.text}")
    
    @allure.step("Удалить тестового пользователя")
    def delete_test_user(self):
        """Удаление тестового пользователя"""
        if self.token:
            headers = {"Authorization": self.token}
            try:
                response = requests.delete(f"{self.base_url}/auth/user", headers=headers, timeout=10)
                if response.status_code == 200:
                    allure.attach("Пользователь удален", name="User Deleted")
                else:
                    allure.attach(f"Не удалось удалить пользователя: {response.text}", name="Delete Warning")
            except Exception as e:
                allure.attach(f"Ошибка при удалении пользователя: {str(e)}", name="Delete Error")
                pass  # Игнорируем ошибки при удалении
    
    @allure.step("Авторизоваться")
    def login(self, email, password):
        """Авторизация пользователя"""
        data = {"email": email, "password": password}
        try:
            response = requests.post(f"{self.base_url}/auth/login", json=data, timeout=10)
            if response.status_code == 200:
                user_data = response.json()
                self.token = user_data.get("accessToken")
                allure.attach(f"Успешная авторизация: {email}", name="Login Success")
                return user_data
            else:
                allure.attach(f"Ошибка авторизации: {response.text}", name="Login Error")
                return None
        except Exception as e:
            allure.attach(f"Исключение при авторизации: {str(e)}", name="Login Exception")
            return None
    
    @allure.step("Создать заказ")
    def create_order(self, ingredients=None, token=None):
        """Создание заказа через API"""
        headers = {}
        if token:
            headers["Authorization"] = token
        elif self.token:
            headers["Authorization"] = self.token
        
        # Используем правильные ID из полученного списка
        # ID из вывода get_ingredients.py:
        # 61c0c5a71d1f82001bdaaa6d - Флюоресцентная булка R2-D3 (bun)
        # 61c0c5a71d1f82001bdaaa72 - Соус Spicy-X (sauce)
        # 61c0c5a71d1f82001bdaaa70 - Говяжий метеорит (main)
        
        if ingredients is None:
            ingredients = ["61c0c5a71d1f82001bdaaa6d", "61c0c5a71d1f82001bdaaa72"]  # Булка + соус
        
        data = {"ingredients": ingredients}
        
        try:
            allure.attach(f"Создание заказа с ингредиентами: {ingredients}", name="Order Creation")
            response = requests.post(f"{self.base_url}/orders", json=data, headers=headers, timeout=10)
            
            response_data = response.json()
            allure.attach(f"Ответ API: {response_data}", name="API Response")
            allure.attach(f"Код ответа: {response.status_code}", name="Status Code")
            
            return response_data
        except Exception as e:
            error_msg = f"Исключение при создании заказа: {str(e)}"
            allure.attach(error_msg, name="Order Exception")
            return {"success": False, "message": error_msg}
    
    @allure.step("Получить информацию о пользователе")
    def get_user_info(self, token=None):
        """Получение информации о пользователе"""
        headers = {}
        if token:
            headers["Authorization"] = token
        elif self.token:
            headers["Authorization"] = self.token
        
        try:
            response = requests.get(f"{self.base_url}/auth/user", headers=headers, timeout=10)
            return response.json()
        except Exception as e:
            return {"success": False, "message": str(e)}
    
    @allure.step("Обновить информацию о пользователе")
    def update_user_info(self, name=None, email=None, password=None, token=None):
        """Обновление информации о пользователе"""
        headers = {}
        if token:
            headers["Authorization"] = token
        elif self.token:
            headers["Authorization"] = self.token
        
        data = {}
        if name:
            data["name"] = name
        if email:
            data["email"] = email
        if password:
            data["password"] = password
        
        try:
            response = requests.patch(f"{self.base_url}/auth/user", json=data, headers=headers, timeout=10)
            return response.json()
        except Exception as e:
            return {"success": False, "message": str(e)}
    
    @allure.step("Получить список ингредиентов")
    def get_ingredients(self):
        """Получение списка ингредиентов"""
        try:
            response = requests.get(f"{self.base_url}/ingredients", timeout=10)
            if response.status_code == 200:
                data = response.json()
                # Сохраняем список для возможного использования
                self.ingredients = data.get("data", [])
                return data
            return {"success": False, "message": f"Код ответа: {response.status_code}"}
        except Exception as e:
            return {"success": False, "message": str(e)}
    
    @allure.step("Получить заказы пользователя")
    def get_user_orders(self, token=None):
        """Получение заказов пользователя"""
        headers = {}
        if token:
            headers["Authorization"] = token
        elif self.token:
            headers["Authorization"] = self.token
        
        try:
            response = requests.get(f"{self.base_url}/orders", headers=headers, timeout=10)
            return response.json()
        except Exception as e:
            return {"success": False, "message": str(e)}
    
    @allure.step("Получить все заказы")
    def get_all_orders(self):
        """Получение всех заказов (лента заказов)"""
        try:
            response = requests.get(f"{self.base_url}/orders/all", timeout=10)
            return response.json()
        except Exception as e:
            return {"success": False, "message": str(e)}