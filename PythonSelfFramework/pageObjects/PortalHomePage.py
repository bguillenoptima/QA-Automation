from selenium.webdriver.common.by import By

from pageObjects.SignaturePage import SignaturePage


class PortalHomePage:

    def __init__(self, driver):
        self.driver = driver

    acknowledge = (By.XPATH, "//button[contains(text(), 'Acknowledge')]")
    getStarted = (By.XPATH, "//button[contains(text(), 'Started')]")
    agree = (By.LINK_TEXT, "I Agree")
    accountDropdown = (By.CSS_SELECTOR, "a[id='accountDropdown']")
    logOut = (By.PARTIAL_LINK_TEXT, "Log out")

    def account_drop_down(self):
        return self.driver.find_element(*PortalHomePage.accountDropdown)

    def log_out(self):
        return self.driver.find_element(*PortalHomePage.logOut)

    def portal_acknowledge(self):
        return self.driver.find_element(*PortalHomePage.acknowledge)

    def portal_get_started(self):
        return self.driver.find_element(*PortalHomePage.getStarted)

    def portal_agree(self):
        self.driver.find_element(*PortalHomePage.agree).click()
        signaturePage = SignaturePage(self.driver)
        return signaturePage




