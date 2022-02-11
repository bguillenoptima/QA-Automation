from selenium.webdriver.common.by import By

class SfHomePage:

    def __init__(self, driver):
        self.driver = driver

    createDataButton = (By.XPATH, "//div[@class='slds-card__body']/button")
    nameField = ()

    def create_data_button(self):
        return self.driver.find_element(*SfHomePage.createDataButton)
    def name_field(self):
        return
