# импортируем модули и отдельные классы
import pytest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture(scope="function")
def driver():
    # Опции браузера
    options = webdriver.ChromeOptions()
    options.page_load_strategy = "normal"  # ожидает загрузки всех ресурсов (картинки, js-код, шрифты и т.д) на странице
    options.add_argument("--headless")  # спец. режим "без браузера"
    options.add_argument(
        "--window-size=1280,1080"
    )  # устанавливает размер окна браузера
    options.add_argument("--disable-infobars")  # отключаем инфо сообщения
    options.add_argument("--disable-extensions")  # отключаем расширения
    options.add_argument(
        "--ignore-certificate-errors"
    )  # Игнорирование ошибок сертификатов
    options.add_argument("--disable-cache")  # Отключение кеширования
    options.add_argument(
        "--disable-search-engine-choice-screen"
    )  # отключаем выбор движка для поиска
    options.add_argument("--disable-dev-shm-usage") # Решает проблему с нехваткой памяти в контейнере
    options.add_argument("--no-sandbox")     # Обязательно для Docker

    # Инициализация драйвера
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)

    yield driver

    driver.quit()
