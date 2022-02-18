from selenium.webdriver.common.by import By
from pageObjects.PaymentAuthorizationPages import PaymentAuthorization


class RequestForTranscript:

    def __init__(self, driver):
        self.driver = driver

    viewForm = (By.XPATH, "//div[@class='container']/div/div/div[2]/a")
    image = (By.XPATH, "//div[@id='form-preview-modal']/div/div/div[2]/img")
    xButton = (By.CSS_SELECTOR, "button[class='close']")
    continueButton = (By.CSS_SELECTOR, "[class*='btn-success']")

    def view_form_elements(self):
        return self.driver.find_elements(*RequestForTranscript.viewForm)

    def form_image(self):
        return self.driver.find_element(*RequestForTranscript.image)

    def x_button(self):
        return self.driver.find_element(*RequestForTranscript.xButton)

    def continue_button(self):
        self.driver.find_element(*RequestForTranscript.continueButton).click()
        paymentAuth = PaymentAuthorization(self.driver)
        return paymentAuth





