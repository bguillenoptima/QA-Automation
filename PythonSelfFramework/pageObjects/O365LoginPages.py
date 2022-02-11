from selenium.webdriver.common.by import By

class O365LoginPages:

    def __init__(self, driver):
        self.driver = driver

    emailField = (By.CSS_SELECTOR, "input[name='loginfmt']")
    nextButton = (By.CSS_SELECTOR, "input[type='submit']")
    passwordField = (By.CSS_SELECTOR, "input[type='password']")

    def email_field(self, email):
        self.driver.find_element(*O365LoginPages.emailField).send_keys(email)

    def next_button(self):
        return self.driver.find_element(*O365LoginPages.nextButton)

    def password_field(self):
        self.driver.find_element(*O365LoginPages.passwordField).send_keys("Opti%6&8$")

