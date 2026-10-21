import pytest
from playwright.sync_api import APIRequestContext

@pytest.mark.api
def test_api_generate_sharing_uuid(api_request_context: APIRequestContext):
    """Поток 4: Проверка генерации UUID-токена для шеринга сборки"""
    payload = {
        "location": "Горнолыжный курорт",
        "dates": ["2026-12-01", "2026-12-10"],
        "guests": {"adults": 2, "children": 0}
    }
    
    # Делаем запрос к API
    response = api_request_context.post("/api/v1/sharing/generate", data=payload)
    
    assert response.ok, f"API вернул ошибку: {response.status}"
    data = response.json()
    
    # Проверка обязательных полей по ТЗ
    assert "share_id" in data, "Бэкенд не вернул share_id"
    assert len(data["share_id"]) == 36, "Поле share_id не является валидным UUID (длина должна быть 36 символов)"
