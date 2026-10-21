import pytest
from playwright.sync_api import Page, expect
from pages.configurator_page import ConfiguratorPage

@pytest.mark.ui
def test_successful_form_reset_on_prod(page: Page):
    """Альтернативный поток 1: Сброс параметров формы и обнуление прогресс-бара"""
    config_page = ConfiguratorPage(page)
    
    # 1. Открываем рабочий стенд
    config_page.open()
    
    # 2. Заполняем поле (выбираем горнолыжный курорт)
    config_page.select_resort("Горнолыжный курорт")
    
    # 3. Вызываем сброс и соглашаемся в модальном окне
    config_page.trigger_reset()
    config_page.confirm_reset()
    
    # 4. Проверяем состояние интерфейса согласно требованиям ТЗ
    expect(config_page.progress_bar).to_contain_text("0%")
    expect(config_page.checkout_button).to_be_disabled()
