
from selenium.webdriver.common.by import By

from pageObjects.SfInvOpportunity import SalesForceInvOpportunityPage


class LeadPage:

    def __init__(self, driver):
        self.driver = driver

    primaryPhoneEditPencil = (By.XPATH, "//button[@title='Edit Phone, Primary']/lightning-primitive-icon")
    phoneNumber = (By.XPATH, "//a[contains(text(), 'Contact Details')]/parent::h2/parent::div/parent::div/parent::div/parent::div/div[2]/div/div/div[2]/div/section/div[2]/div/div[1]/div/div/div/div/div[2]/div[1]/div/div/div/input")
    saveButton = (By.XPATH, "//button[@title='Save']")
    convertButton = (By.XPATH, "//button[contains(text(),'Convert')]")
    conversionSaveButton = (By.XPATH, "//button[contains(text(),'Save')]")
    conversionReadinessPhone = (By.CSS_SELECTOR, "h3[title='Phone']")


    def phone_edit_pencil(self):
        return self.driver.find_element(*LeadPage.primaryPhoneEditPencil)

    def phone_number(self):
        return self.driver.find_element(*LeadPage.phoneNumber)

    def contact_details_save(self):
        return self.driver.find_element(*LeadPage.saveButton)

    def convert_button(self):
        return self.driver.find_element(*LeadPage.convertButton)

    def conversion_readiness_phone(self):
        return self.driver.find_element(*LeadPage.conversionReadinessPhone)

    def lead_conversion_save(self):
        conversionSaveButton = self.driver.find_element(*LeadPage.conversionSaveButton)
        self.driver.execute_script("arguments[0].click();", conversionSaveButton)
        inv_opportunity = SalesForceInvOpportunityPage(self.driver)
        return inv_opportunity




