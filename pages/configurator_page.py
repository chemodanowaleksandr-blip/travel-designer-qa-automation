from playwright.sync_api import Page, Locator

class ConfiguratorPage:
    def __init__(self, page: Page):
        self.page = page
        
        # --- Основная форма конфигуратора ---
        self.city_start = page.get_by_placeholder("Город старта")
        self.city_arrival = page.get_by_placeholder("Город прилёта")
        
        # Селектор выбора курорта (ищем по тексту, так как это кастомный dropdown)
        self.location_dropdown = page.locator("text=Выбрать локацию").first
        self.reset_button = page.locator("button", has_text="Сбросить")
        
        # --- Модальное окно подтверждения сброса (Альтернативный поток 1) ---
        self.modal_window = page.locator("[class*='modal'], [class*='popup']").filter(has_text="Вы уверены")
        self.confirm_reset_btn = page.locator("button", has_text="Да")
        self.cancel_reset_btn = page.locator("button", has_text="Нет")
        
        # --- Прогресс-бар и финал ---
        self.progress_bar = page.locator("[class*='progress-bar'], [class*='progress']").first
        self.checkout_button = page.locator("button", has_text="К оформлению")

    def open(self):
        """Открытие конфигуратора по реальному адресу"""
        self.page.goto("/trip-builder")
        self.page.wait_for_load_state("networkidle")

    def select_resort(self, resort_name: str):
        """Выбор горнолыжного курорта"""
        self.location_dropdown.click()
        self.page.locator(f"text={resort_name}").click()

    def trigger_reset(self):
        """Нажатие на сброс"""
        self.reset_button.click()

    def confirm_reset(self):
        """Подтверждение сброса в модалке"""
        self.confirm_reset_btn.click()
