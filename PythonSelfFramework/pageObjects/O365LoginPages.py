from selenium.webdriver.common.by import By

from pageObjects.SfHomePage import SalesForceHomePage


class O365LoginPages:

    def __init__(self, driver):
        self.driver = driver

    emailField = (By.CSS_SELECTOR, "input[name='loginfmt']")
    nextButton = (By.CSS_SELECTOR, "input[type='submit']")
    passwordField = (By.CSS_SELECTOR, "input[type='password']")
    otpField = (By.NAME, "otc")
    o365Button = (By.CSS_SELECTOR, "button[class='button mb24 secondary wide']")

    def email_field(self):
        return self.driver.find_element(*O365LoginPages.emailField)

    def next_button(self):
        return self.driver.find_element(*O365LoginPages.nextButton)

    def password_field(self):
        return self.driver.find_element(*O365LoginPages.passwordField)

    def otp_field(self):
        return self.driver.find_element(*O365LoginPages.otpField)

    def office_365_button(self):
        self.driver.find_element(*O365LoginPages.o365Button).click()
        sfHomePage = SalesForceHomePage(self.driver)
        return sfHomePage

