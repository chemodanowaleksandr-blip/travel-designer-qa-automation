import pytest
import allure
import requests

@allure.epic("Платформа Travel Designer")
@allure.feature("API Интеграции")
@allure.story("Генерация ссылки для шеринга")
@allure.title("Запрос UUID-токена для создания постоянной ссылки")
@pytest.mark.api
@pytest.mark.xfail(reason="Бэкенд возвращает 404 согласно bug-11")
def test_api_generate_sharing_uuid(base_url):
    payload = {
        "location": "Горнолыжный курорт",
        "dates": ["2026-12-01", "2026-12-10"],
        "guests": {"adults": 2, "children": 0}
    }
    with allure.step("Отправка POST запроса на генерацию ссылки"):
        response = requests.post(f"{base_url}/api/v1/sharing/generate", json=payload)
    
    with allure.step("Проверка успешности ответа (код 200)"):
        assert response.status_code == 200
