from selenium.webdriver.common.by import By

from pageObjects.O365PwPage import O365PwPage


class O365EmailPage:

    def __init__(self, driver):
        self.driver = driver

    email = (By.CSS_SELECTOR, "input[name='loginfmt']")
    next_Button = (By.CSS_SELECTOR, "input[type='submit']")

    def email_items(self):
        self.driver.find_element(*O365EmailPage.email).send_keys("bguillen@optimataxrelief.com")

    def email_next_button(self):
        self.driver.find_element(*O365EmailPage.next_Button).click()
        office_pw_page = O365PwPage(self.driver)
        return office_pw_page

