from selenium.webdriver.common.by import By
from pageObjects.RequestForTranscriptPage import RequestForTranscript



class TaxInformationAuthorization:

    def __init__(self, driver):
        self.driver = driver

    viewForm = (By.PARTIAL_LINK_TEXT, "View")
    image = (By.XPATH, "//div[@id='form-preview-modal']/div/div/div[2]/img")
    xButton = (By.CSS_SELECTOR, "button[class='close']")
    continueButton = (By.CSS_SELECTOR, "[class*='btn-success']")

    def view_form(self):
        return self.driver.find_element(*TaxInformationAuthorization.viewForm)

    def form_image(self):
        return self.driver.find_element(*TaxInformationAuthorization.image)

    def x_button(self):
        return self.driver.find_element(*TaxInformationAuthorization.xButton)

    def continue_button(self):
        self.driver.find_element(*TaxInformationAuthorization.continueButton).click()
        requestForTranscript = RequestForTranscript(self.driver)
        return requestForTranscript
















