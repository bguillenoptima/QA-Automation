from selenium.webdriver.common.by import By


class O365HomePage:

    def __init__(self, driver):
        self.driver = driver

    waffle = (By.CSS_SELECTOR, "button[id='O365_MainLink_NavMenu']")
    sf_dev = (By.CSS_SELECTOR, "a[aria-label='Salesforce (Dev)']")

    def waffle_icon(self):
        return self.driver.find_element(*O365HomePage.waffle)

    def sf_dev_button(self):
        self.driver.find_element(*O365HomePage.sf_dev).click()
        #may need to insert a wait until SF page loads
        self.driver.execute_script("window.open('about:blank','disposable_email');")
        self.driver.execute_script("window.open('about:blank','disposable_email');")
        self.driver.switch_to.window("disposable_email")
        self.driver.get("https://www.disposablemail.com/")


