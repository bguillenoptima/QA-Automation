from selenium.webdriver.common.by import By


class O365PwMultiAuth:

    def __init__(self, driver):
        self.driver = driver

    verify = (By.CSS_SELECTOR, "input[type='submit']")

    def click_verify(self):
        self.driver.find_element(*O365PwMultiAuth.verify).click()
