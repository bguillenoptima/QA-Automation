
from selenium.webdriver.common.by import By



class PasswordCreate:

    def __init__(self, driver):
        self.driver = driver

    portalPassword = (By.NAME, "password")
    portalConfirmPassword = (By.NAME, "password_confirmation")

    def portal_password(self):
        return self.driver.find_element(*PasswordCreate.portalPassword)

    def confirm_password(self):
        return self.driver.find_element(*PasswordCreate.portalConfirmPassword)





