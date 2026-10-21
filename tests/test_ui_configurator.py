import pytest
import allure
from playwright.sync_api import Page, expect

@allure.epic("Платформа Travel Designer")
@allure.feature("Конфигуратор тура")
@allure.story("Сброс параметров формы")
@allure.title("Проверка полной очистки формы и обнуления прогресс-бара")
@pytest.mark.ui
def test_successful_form_reset_on_prod(page: Page):
    with allure.step("1. Открытие страницы конфигуратора"):
        response = page.goto("https://elmobil.ru", timeout=30000)
        if not response or response.status != 200:
            pytest.skip("Сайт недоступен")
        page.wait_for_load_state("networkidle")

    with allure.step("2. Выбор горнолыжного курорта"):
        page.locator("text=Выбрать локацию").first.click()
        page.locator("text=Горнолыжный курорт").click()

    with allure.step("3. Нажатие кнопки 'Сбросить' и подтверждение"):
        page.locator("button", has_text="Сбросить").click()
        page.locator("button", has_text="Да").click()

    with allure.step("4. Валидация ОР: Прогресс-бар равен 0%"):
        progress_bar = page.locator("[class*='progress']").first
        expect(progress_bar).to_contain_text("0%")
