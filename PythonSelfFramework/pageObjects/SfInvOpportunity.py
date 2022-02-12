from selenium.webdriver.common.by import By


class SalesForceInvOpportunityPage:

    def __init__(self, driver):
        self.driver = driver

    paymentScheduleButton = (By.XPATH, "//button[contains(text(), 'Create Pmt Schedules')]")

    def payment_schedule_button(self):
        return self.driver.find_element(*SalesForceInvOpportunityPage.paymentScheduleButton)



