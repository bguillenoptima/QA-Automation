from selenium.webdriver.common.by import By


class DisposableEmailPage:

    email = (By.CSS_SELECTOR, "span[id='email']")

    def __init__(self, driver):
        self.driver = driver

    def store_email(self):
        return self.driver.find_element(*DisposableEmailPage.email).text
