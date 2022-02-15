from selenium.webdriver.common.by import By

from pageObjects.LeadPage import LeadPage


class SalesForceHomePage:

    def __init__(self, driver):
        self.driver = driver

    createDataButton = (By.XPATH, "//div[@class='slds-card__body']/button")

    def nav_console_home(self):
        return self.driver.find_element.click()



