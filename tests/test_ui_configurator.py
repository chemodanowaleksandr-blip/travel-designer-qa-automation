import pytest
from playwright.sync_api import Page, expect

@pytest.mark.ui
def test_successful_form_reset_on_prod(page: Page):
    """Альтернативный поток 1: Сброс параметров формы и обнуление прогресс-бара"""
    
    # 1. Открываем рабочий стенд
    page.goto("https://elmobil.ru")
    
    # Ждем, пока на странице появится хотя бы одно из основных полей ввода
    page.wait_for_selector("input", timeout=15000)
    
    # 2. Вместо кастомного клика по локации, заполняем стандартное текстовое поле "Город старта"
    # Ищем поле ввода, где в плейсхолдере или подсказке есть слово "старт" или "Откуда"
    city_input = page.locator("input[placeholder*='старт'], input[placeholder*='Откуда'], input[type='text']").first
    city_input.fill("Москва")
    city_input.press("Enter")
    
    # Даем 1 секунду на перерасчет прогресс-бара фронтендом
    page.wait_for_timeout(1000)
    
    # 3. Находим кнопку "Сбросить" и кликаем по ней
    # Используем гибкий селектор, чтобы поймать кнопку в любом регистре
    reset_button = page.locator("button:has-text('Сбросить'), button:has-text('сбросить')").first
    reset_button.click()
    
    # 4. В модальном окне подтверждения кликаем "Да"
    confirm_button = page.locator("button:has-text('Да'), button:has-text('Подтвердить')").first
    confirm_button.click()
    
    # 5. Проверяем состояние интерфейса согласно требованиям ТЗ
    # Ищем прогресс-бар по частичному совпадению классов
    progress_bar = page.locator("[class*='progress']").first
    checkout_button = page.locator("button:has-text('оформлению'), button:has-text('Оформить')").first
    
    # Проверяем, что форма обнулилась
    expect(progress_bar).to_contain_text("0%")
