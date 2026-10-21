import pytest
from playwright.sync_api import APIRequestContext

@pytest.mark.api
def test_api_generate_sharing_uuid(api_request_context: APIRequestContext):
    """Поток 4: Валидация создания постоянной ссылки через API"""
    payload = {
        "location": "Горнолыжный курорт",
        "dates": ["2026-12-01", "2026-12-10"],
        "guests": {"adults": 2, "children": 0}
    }
    
    # Отправляем POST-запрос на эндпоинт генерации ссылки
    response = api_request_context.post("/api/v1/sharing/generate", data=payload)
    
    assert response.ok, f"Запрос завершился с ошибкой: {response.status}"
    data = response.json()
    
    # Строгие проверки структуры данных по ТЗ
    assert "share_id" in data, "В ответе API отсутствует share_id"
    assert len(data["share_id"]) == 36, "Формат токена не соответствует UUID (длина должна быть 36 символов)"
