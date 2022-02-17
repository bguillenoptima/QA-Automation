
from selenium.webdriver.common.by import By

from pageObjects.InformationVerificationPage import InformationVerificationPage


class SignaturePage:

    def __init__(self, driver):
        self.driver = driver

    canvas = (By.CSS_SELECTOR, "div[class*='pad--body'] canvas")
    submit = (By.XPATH, "//button[contains(text(),'Submit')]")

    def portal_canvas(self):
        return self.driver.find_element(*SignaturePage.canvas)

    def portal_sign(self):
        return

    def portal_submit(self):
        submit_button = self.driver.find_element(*SignaturePage.submit)
        self.driver.execute_script("arguments[0].click();", submit_button)
        verificationPage = InformationVerificationPage(self.driver)
        return verificationPage









