from selenium.webdriver.common.by import By

from pageObjects.O365PwMultiAuth import O365PwMultiAuth


class O365PwPage:

    def __init__(self, driver):
        self.driver = driver

    password = (By.CSS_SELECTOR, "input[type='password']")
    password_Next = (By.CSS_SELECTOR, "input[type='submit']")

    def send_password(self):
        self.driver.find_element(*O365PwPage.password).send_keys("Opti%6&8$")

    def password_next(self):
        self.driver.find_element(*O365PwPage.password_Next).click()
        office_multi_factor_auth = O365PwMultiAuth(self.driver)
        return office_multi_factor_auth
