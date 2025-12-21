import httpx  # Импортируем библиотеку HTTPX

# Данные для входа в систему
login_payload = {"email": "user@example.com", "password": "string"}

# Выполняем запрос на аутентификацию
login_response = httpx.post(
    "http://localhost:8000/api/v1/authentication/login", json=login_payload
)
login_response_data = login_response.json()

# Выводим полученные токены
print("Login response:", login_response_data)
print("Status Code:", login_response.status_code)

get_user_headers = {
    "Authorization": f"Bearer {login_response_data['token']['accessToken']}"
}
get_user_response = httpx.get(
    "http://localhost:8000/api/v1/users/me", headers=get_user_headers
)
get_user_response_data = get_user_response.json()

# Выводим обновленные токены
print("Get user response:", get_user_response_data)
print("Get user status code:", get_user_response.status_code)
