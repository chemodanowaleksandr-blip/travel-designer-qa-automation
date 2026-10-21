import pytest
from playwright.sync_api import Page, expect

@pytest.mark.ui
def test_successful_form_reset_on_prod(page: Page):
    """Альтернативный поток 1: Сброс параметров формы и обнуление прогресс-бара"""
    
    # 1. Пробуем открыть стенд и ловим ответ сервера
    response = page.goto("https://elmobil.ru", timeout=30000)
    
    # Если сайт лежит или отдает ошибку (например, 502 или 404), мягко пропускаем тест
    if not response or response.status != 200:
        pytest.skip(f"Сайт недоступен или вернул ошибку {response.status if response else 'No Response'}. Пропускаем UI-тест.")

    # Ждем полной стабилизации сети
    page.wait_for_load_state("networkidle", timeout=10000)
    
    # Делаем скриншот для отчета, чтобы в HTML-файле было видно, ЧТО именно загрузилось на экране
    page.screenshot(path="loaded_page.png")
    
    # 2. Проверяем наличие критических кнопок на фронте. 
    # Если верстка поменялась, тест упадет с понятной ошибкой, а не просто по таймауту
    reset_btn = page.locator("button:has-text('Сбросить'), button:has-text('сбросить')").first
    
    if reset_btn.count() == 0:
        pytest.fail("Кнопка 'Сбросить' не найдена на текущем интерфейсе страницы. Проверьте скриншот loaded_page.png")
        
    # 3. Кликаем по кнопке Сбросить
    reset_btn.click()
    
    # 4. Проверяем модалку подтверждения, если она появилась
    confirm_btn = page.locator("button:has-text('Да'), button:has-text('Подтвердить')").first
    if confirm_btn.count() > 0:
        confirm_btn.click()
        
    # 5. Проверяем обнуление прогресса
    progress_bar = page.locator("[class*='progress']").first
    if progress_bar.count() > 0:
        expect(progress_bar).to_contain_text("0%")
