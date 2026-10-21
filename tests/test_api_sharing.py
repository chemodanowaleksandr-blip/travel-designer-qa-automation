import pytest
import requests

@pytest.mark.api
@pytest.mark.xfail(reason="Бэкенд возвращает 404 Not Found согласно баг-репорту bug-11")
def test_api_generate_sharing_uuid(base_url):
    """Поток 4: Проверка генерации UUID-токена для шеринга сборки"""
    payload = {
        "location": "Горнолыжный курорт",
        "dates": ["2026-12-01", "2026-12-10"],
        "guests": {"adults": 2, "children": 0}
    }
    
    # Отправляем запрос через стандартный requests
    response = requests.post(f"{base_url}/api/v1/sharing/generate", json=payload)
    assert response.status_code == 200
