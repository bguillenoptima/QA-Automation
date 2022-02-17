from selenium.webdriver.common.by import By
from pageObjects.PasswordCreatePage import PasswordCreate


class DisposableEmailPage:

    def __init__(self, driver):
        self.driver = driver

    email = (By.CSS_SELECTOR, "span[id='email']")
    welcomeEmail = (By.XPATH, "//td[contains(text(),'Welcome to Optima Tax Relief')]")
    deleteLink = (By.LINK_TEXT, "Delete")

    def store_email(self):
        return self.driver.find_element(*DisposableEmailPage.email)

    def welcome_email(self):
        return self.driver.find_element(*DisposableEmailPage.welcomeEmail)

    def delete_email(self):
        return self.driver.find_element(*DisposableEmailPage.deleteLink)

    def welcome_email_create_link(self):
        self.driver.find_element(By.LINK_TEXT, "Create Account →").click()
        createPasswordPage = PasswordCreate(self.driver)
        return createPasswordPage






