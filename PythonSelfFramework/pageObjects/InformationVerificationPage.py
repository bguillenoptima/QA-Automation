from selenium.webdriver.common.by import By

from pageObjects.ServiceAgreementPage import ServiceAgreementPage


class InformationVerificationPage:

    def __init__(self, driver):
        self.driver = driver

    ssn = (By.CSS_SELECTOR, "input[name='masked_tax_identification_number']")
    dobDropDowns = (By.CSS_SELECTOR, "select[name*='birth']")
    verify = (By.CSS_SELECTOR, "button[id='show-confirmation-modal']")
    confirmButton = (By.CSS_SELECTOR,"button[id='forms-nav-verify']")

    def ssn_field(self):
        return self.driver.find_element(*InformationVerificationPage.ssn)

    def dob_drop_downs(self):
        return self.driver.find_elements(*InformationVerificationPage.dobDropDowns)

    def verify_button(self):
        return self.driver.find_element(*InformationVerificationPage.verify)

    def confirm_button(self):
        self.driver.find_element(*InformationVerificationPage.confirmButton).click()
        serviceAgreementPage = ServiceAgreementPage(self.driver)
        return serviceAgreementPage













