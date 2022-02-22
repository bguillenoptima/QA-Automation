from selenium.webdriver.common.by import By


class AdminOpportunities:

    def __init__(self, driver):
        self.driver = driver

    searchField = (By.CSS_SELECTOR, "input[id='search']")
    invOpp = (By.PARTIAL_LINK_TEXT, "Opportunity")
    paymentAuthorization = (By.XPATH, "//div[@id='forms-tab']/div[2]/table/tbody/tr[9]/td[5]")
    paymentApproval = (By.PARTIAL_LINK_TEXT, "Approve")
    servicesLink = (By.PARTIAL_LINK_TEXT, "Services")
    paymentsTab = (By.PARTIAL_LINK_TEXT, "Payments")
    paymentsSchedule = (By.PARTIAL_LINK_TEXT, "Payment Schedule")
    payNow = (By.XPATH, "//button[contains(text(),'Pay Now')]")
    processPayment = (By.CSS_SELECTOR, "button[data-form-id='pay-now-otr-form']")


    def inv_opportunity(self):
        return self.driver.find_element(*AdminOpportunities.invOpp)

    def payment_authorization(self):
        return self.driver.find_element(*AdminOpportunities.paymentAuthorization)

    def payment_approval(self):
        return self.driver.find_element(*AdminOpportunities.paymentApproval)

    def services_link(self):
        return self.driver.find_element(*AdminOpportunities.servicesLink)

    def payments_tab(self):
        return self.driver.find_element(*AdminOpportunities.paymentsTab)

    def payments_schedule(self):
        return self.driver.find_element(*AdminOpportunities.paymentsSchedule)

    def pay_now(self):
        return self.driver.find_element(*AdminOpportunities.payNow)

    def process_payment(self):
        return self.driver.find_element(*AdminOpportunities.processPayment)


