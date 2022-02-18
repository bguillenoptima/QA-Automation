from selenium.webdriver.common.by import By


class ServiceAgreementPages:

    def __init__(self, driver):
        self.driver = driver

    viewForm = (By.PARTIAL_LINK_TEXT, "View")
    readMore = (By.LINK_TEXT, "read more...")
    paragraphs = (By.CSS_SELECTOR, "div[class='more'] p")
    xButton = (By.CSS_SELECTOR, "button[class='close']")
    continueButton = (By.CSS_SELECTOR, "[class*='btn-success']")

    def view_form_button(self):
        return self.driver.find_element(*ServiceAgreementPages.viewForm)

    def read_more_button(self):
        return self.driver.find_element(*ServiceAgreementPages.readMore)

    def content(self):
        return self.driver.find_elements(*ServiceAgreementPages.paragraphs)

    def x_button(self):
        return self.driver.find_element(*ServiceAgreementPages.xButton)

    def continue_button(self):
        return self.driver.find_element(*ServiceAgreementPages.continueButton)














