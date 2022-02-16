
from selenium.webdriver.common.by import By

from pageObjects.PortalHomePage import PortalHomePage


class PasswordCreate:

    def __init__(self, driver):
        self.driver = driver

    portalPassword = (By.NAME, "password")
    portalConfirmPassword = (By.NAME, "password_confirmation")
    portalCreateAccount = (By.CSS_SELECTOR, "button[id='login-btn'")

    def portal_password(self):
        return self.driver.find_element(*PasswordCreate.portalPassword)

    def confirm_password(self):
        return self.driver.find_element(*PasswordCreate.portalConfirmPassword)

    def create_account(self):
        self.driver.find_element(*PasswordCreate.portalCreateAccount).click()
        homePage = PortalHomePage(self.driver)
        return homePage






