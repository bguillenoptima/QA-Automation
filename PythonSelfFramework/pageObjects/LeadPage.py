from selenium.webdriver.common.by import By


class LeadPage:

    def __init__(self, driver):
        self.driver = driver

    primaryPhoneEditPencil = (By.XPATH, "//button[@title='Edit Phone, Primary']/lightning-primitive-icon")
    phoneNumber = (By.XPATH, "//a[contains(text(), 'Contact Details')]/parent::h2/parent::div/parent::div/parent::div/parent::div/div[2]/div/div/div[2]/div/section/div[2]/div/div[1]/div/div/div/div/div[2]/div[1]/div/div/div/input")
    saveButton = (By.XPATH, "//button[@title='Save']")

    def phone_edit_pencil(self):
        return self.driver.find_element(*LeadPage.primaryPhoneEditPencil)

    def phone_number(self):
        return self.driver.find_element(*LeadPage.phoneNumber)

    def contact_details_save(self):
        return self.driver.find_element(*LeadPage.saveButton)