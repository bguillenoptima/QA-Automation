from selenium.webdriver.common.by import By


class PaymentAuthorization:

    def __init__(self, driver):
        self.driver = driver

    signer = (By.XPATH, "//div[@id='signers']/button[1]")
    image = (By.XPATH, "//div[@id='form-preview-modal']/div/div/div[2]/img")
    xButton = (By.CSS_SELECTOR, "button[class='close']")
    continueButton = (By.CSS_SELECTOR, "[class*='btn-success']")
    viewForm = (By.PARTIAL_LINK_TEXT, "View")

    def view_form(self):
        return self.driver.find_element(*PaymentAuthorization.viewForm)

    def form_image(self):
        return self.driver.find_element(*PaymentAuthorization.image)

    def x_button(self):
        return self.driver.find_element(*PaymentAuthorization.xButton)

    def continue_button(self):
        return self.driver.find_element(*PaymentAuthorization.continueButton).click()

    def payment_signer(self):
        return self.driver.find_element(*PaymentAuthorization.signer)

















