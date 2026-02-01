import pytest
import requests

from selenium.webdriver.chrome.webdriver import WebDriver
from Login_page import LoginPage


@pytest.mark.parametrize("user, password", [("standard_user","secret_sauce"), ("performance_glitch_user", "secret_sauce")])
def test_positive_login(driver: WebDriver, user, password):
    """
    Test-case-1 Авторизация успешная
    """
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login(user, password)

    assert "inventory.html" in driver.current_url, "Переход на страницу магазина не удался"

@pytest.mark.parametrize("user, password", [("standard_user","incorrect_pass"), ("locked_out_user", "secret_sauce"), ("", "")])
def test_negative_login(driver: WebDriver, user, password):
    """
    Test-case-2 Авторизация неуспешная
    """
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login(user, password)

    assert driver.current_url == "https://www.saucedemo.com/", "Переход на страницу магазина удался"
