from selenium.webdriver.common.by import By

from pageObjects.O365PwPage import O365PwPage


class O365LoginPages:

    def __init__(self, driver):
        self.driver = driver

    emailField = (By.CSS_SELECTOR, "input[name='loginfmt']")
    NextButton = (By.CSS_SELECTOR, "input[type='submit']")
    passwordField = (By.CSS_SELECTOR, "input[type='password']")

    def email_field(self):
        return self.driver.find_element(*O365LoginPages.email_Field)

    def next_button(self):
        return self.driver.find_element(*O365LoginPages.next_Button)

    def password_field(self):
        return self.driver.find_element(*O365LoginPages.passwordField).send_keys("Opti%6&8$")

