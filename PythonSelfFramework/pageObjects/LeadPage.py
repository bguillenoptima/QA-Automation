from selenium.webdriver.common.by import By


class LeadPage:

    def __init__(self, driver):
        self.driver = driver

    primaryPhoneEditPencil = (By.CSS_SELECTOR, "span[id='email']")

    def store_email(self):
        return self.driver.find_element(*LeadPage.email)