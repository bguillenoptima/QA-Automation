from selenium.webdriver.common.by import By

from pageObjects import SfHomePage


class O365HomePage:

    def __init__(self, driver):
        self.driver = driver

    waffle = (By.CSS_SELECTOR, "button[id='O365_MainLink_NavMenu']")
    sf_dev = (By.CSS_SELECTOR, "a[aria-label='Salesforce (Dev)']")

    def waffle_icon(self):
        return self.driver.find_element(*O365HomePage.waffle)

    def sf_dev_button(self):
        return self.driver.find_element(*O365HomePage.sf_dev)




