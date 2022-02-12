from selenium.webdriver.common.by import By
import pytest


class DisposableEmailPage:

    def __init__(self, driver):
        self.driver = driver

    email = (By.CSS_SELECTOR, "span[id='email']")

    def store_email(self):
        return self.driver.find_element(*DisposableEmailPage.email)

    def getData(self, request):
        self.openTab("disposable_email","https://www.disposablemail.com/")

        email_Address = self.store_email().text
        first_name_last_name = email_Address.split(".")
        first_Name = first_name_last_name[0].capitalize()
        parsedLastname = first_name_last_name[1].split("@")
        last_Name = parsedLastname[0].capitalize()

        firstName = first_Name
        lastName = last_Name
        email = email_Address
        test_HomePage_data = dict(first_name=firstName, last_name=lastName, client_email_address=email)
        return test_HomePage_data

