from selenium.webdriver.common.by import By


class SalesForceInvOpportunityPage:

    def __init__(self, driver):
        self.driver = driver

    paymentScheduleButton = (By.XPATH, "//button[contains(text(), 'Create Pmt Schedules')]")
    savePayment = (By.CSS_SELECTOR, "input[type = 'submit']")
    manageDocsTab = (By.XPATH, "//ul[@role='tablist']/li[7]/a")
    paymentIframe = (By.CSS_SELECTOR, "div[id='modal-content-id-1'] iframe")
    paymentDateSelector = (By.CSS_SELECTOR, "input[type='date']")

    def payment_schedule_button(self):
        return self.driver.find_element(*SalesForceInvOpportunityPage.paymentScheduleButton)

    def iframe_payment_save_button(self):
        return self.driver.find_element(*SalesForceInvOpportunityPage.savePayment)

    def manage_docs_tab(self):
        return self.driver.find_element(*SalesForceInvOpportunityPage.manageDocsTab)

    def payment_iframe(self):
        return self.driver.find_element(*SalesForceInvOpportunityPage.paymentIframe)

    def payment_date(self):
        return self.driver.find_element(*SalesForceInvOpportunityPage.paymentDateSelector)



