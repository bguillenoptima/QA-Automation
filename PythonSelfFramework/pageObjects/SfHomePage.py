from selenium.webdriver.common.by import By

from pageObjects.LeadPage import LeadPage


class SalesForceHomePage:

    def __init__(self, driver):
        self.driver = driver

    createDataButton = (By.XPATH, "//div[@class='slds-card__body']/button")
    nameField = (By.XPATH, "//div[@id='modal-content-id-1']/div[1]/input")
    emailField = (By.XPATH, "//div[@id='modal-content-id-1']/div[6]/input")
    createDataButtonInForm = (By.CSS_SELECTOR, "button[title='Create Data']")

    def create_data_button(self):
        return self.driver.find_element(*SalesForceHomePage.createDataButton)

    def create_data_name(self):
        return self.driver.find_element(*SalesForceHomePage.nameField)

    def create_data_email(self):
        return self.driver.find_element(*SalesForceHomePage.emailField)

    def create_data_submit(self):
        self.driver.find_element(*SalesForceHomePage.createDataButtonInForm).click()
        leadPage = LeadPage(self.driver)
        return leadPage

