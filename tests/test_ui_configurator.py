import pytest
from playwright.sync_api import Page, expect

@pytest.mark.ui
def test_successful_form_reset_on_prod(page: Page):
    """Альтернативный поток 1: Сброс параметров формы и обнуление прогресс-бара"""
    
    # 1. Открываем рабочий стенд напрямую
    page.goto("https://elmobil.ru")
    page.wait_for_load_state("networkidle")
    
    # 2. Выбираем горнолыжный курорт (клик по выпадашке и элементу)
    page.locator("text=Выбрать локацию").first.click()
    page.locator("text=Горнолыжный курорт").click()
    
    # 3. Вызываем сброс и соглашаемся в модальном окне
    page.locator("button", has_text="Сбросить").click()
    page.locator("button", has_text="Да").click()
    
    # 4. Проверяем состояние интерфейса согласно требованиям ТЗ
    progress_bar = page.locator("[class*='progress-bar'], [class*='progress']").first
    checkout_button = page.locator("button", has_text="К оформлению")
    
    expect(progress_bar).to_contain_text("0%")
    expect(checkout_button).to_be_disabled()
