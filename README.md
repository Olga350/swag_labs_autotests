5 тестов, проверяющих разные сценарии авторизации
Проект по автоматизации тестирования на Python 3.10 с использованием Selenium и Page Object Model.

# Быстрый запуск (Docker)
docker run --rm -v "${PWD}/allure-results:/app/allure-results" olga-buben-tests
# Отчеты Allure
allure serve allure-results
# Запуск локально (без Docker)
Установите зависимости: pip install -r requirements.txt
Запустите тесты: pytest --alluredir=allure-results

