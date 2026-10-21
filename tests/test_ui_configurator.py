import pytest
from playwright.sync_api import Page, expect
from pages.configurator_page import ConfiguratorPage

@pytest.mark.ui
def test_successful_form_reset_on_prod(page: Page):
    """Альтернативный поток 1: Проверка полного сброса параметров и прогресс-бара"""
    config_page = ConfiguratorPage(page)
    
    # 1. Переходим на реальный адрес сайта
    page.goto("https://trip.elmobil.ru/trip-builder")
    
    # 2. Выбираем локацию (горнолыжный курорт), чтобы заполнить форму
    config_page.select_location("Горнолыжный курорт")
    
    # 3. Нажимаем кнопку сброса и подтверждаем действие в модальном окне
    config_page.click_reset()
    config_page.confirm_reset()
    
    # 4. Проверяем ОР из ТЗ: прогресс-бар сброшен, кнопка заблокирована
    expect(config_page.progress_bar).to_have_text("0%")
    expect(config_page.checkout_button).to_be_disabled()
