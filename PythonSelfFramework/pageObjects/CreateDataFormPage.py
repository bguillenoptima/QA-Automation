from selenium.webdriver.common.by import By


class CreateDataPage:

    def __init__(self, driver):
        self.driver = driver

    create_data_button_location = (By.XPATH, "//div[@class='slds-card__body']/button")
    email_field_location = (By.XPATH, "//div[@id='modal-content-id-1']/div[6]/input")
    name_field_location = (By.XPATH, "//div[@id='modal-content-id-1']/div[1]/input")
    create_data_button_location_in_form = (By.CSS_SELECTOR, "button[title='Create Data']")

    def create_data_button(self):
        return self.driver.find_element(*CreateDataPage.create_data_button_location)

    def email_field(self):
        return self.driver.find_element(*CreateDataPage.email_field_location)

    def name_field(self):
        return self.driver.find_element(*CreateDataPage.name_field_location)

    def create_data_button_in_form(self):
        return self.driver.find_element(*CreateDataPage.name_field_location)

