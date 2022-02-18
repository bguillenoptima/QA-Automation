from selenium.webdriver.common.by import By


class PaymentAuthorization:

    def __init__(self, driver):
        self.driver = driver

    signer = (By.XPATH, "//div[@id='signers']/button[1]")
    image = (By.XPATH, "//div[@id='form-preview-modal']/div/div/div[2]/img")
    xButton = (By.CSS_SELECTOR, "button[class='close']")
    continueButton = (By.CSS_SELECTOR, "button[id= 'continue']")
    viewForm = (By.PARTIAL_LINK_TEXT, "View")
    paymentCard = (By.XPATH, "//button[contains(text(),'Credit or Debit Card')]")
    cardNumberField = (By.CSS_SELECTOR, "input[id='cc-number']")
    cvv = (By.CSS_SELECTOR, "input[name='cc_cvv']")
    confirmSchedule = (By.CSS_SELECTOR, "button[id= 'confirm-payment-schedule']")
    applySignature = (By.CSS_SELECTOR, "a[id= 'authorize-btn']")

    def view_form(self):
        return self.driver.find_element(*PaymentAuthorization.viewForm)

    def form_image(self):
        return self.driver.find_element(*PaymentAuthorization.image)

    def x_button(self):
        return self.driver.find_element(*PaymentAuthorization.xButton)

    def continue_button(self):
        return self.driver.find_element(*PaymentAuthorization.continueButton)

    def payment_signer(self):
        return self.driver.find_element(*PaymentAuthorization.signer)

    def card_button(self):
        return self.driver.find_element(*PaymentAuthorization.paymentCard)

    def card_number_field(self):
        return self.driver.find_element(*PaymentAuthorization.cardNumberField)

    def cvv_number_field(self):
        return self.driver.find_element(*PaymentAuthorization.cvv)

    def confirm_schedule_button(self):
        return self.driver.find_element(*PaymentAuthorization.confirmSchedule)

    def apply_signature_button(self):
        return self.driver.find_element(*PaymentAuthorization.applySignature)


















