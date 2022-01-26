from selenium.webdriver.common.by import By


class O365HomePage:

    def __init__(self, driver):
        self.driver = driver

    waffle = (By.CSS_SELECTOR, "button[id='O365_MainLink_NavMenu']")
    sf_dev = (By.CSS_SELECTOR, "a[aria-label='Salesforce (Dev)']")

    def click_waffle(self):
        self.driver.find_element(*O365HomePage.waffle).click()

    def click_sf_dev(self):
        self.driver.find_element(*O365HomePage.sf_dev).click()
