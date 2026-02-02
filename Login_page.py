from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import LoginPageLocators

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10, poll_frequency=1)
        self.url = "https://www.saucedemo.com/"

    def open(self):
        self.driver.get(self.url)

    def login(self, user, password):
        login_field = self.wait.until(EC.element_to_be_clickable(LoginPageLocators.User_Name))
        login_field.click()
        login_field.clear()
        login_field.send_keys(user)

        pass_field = self.wait.until(EC.element_to_be_clickable(LoginPageLocators.Password))
        pass_field.click()
        pass_field.clear()
        pass_field.send_keys(password)

        self.wait.until(EC.element_to_be_clickable(LoginPageLocators.Login_button)).click()