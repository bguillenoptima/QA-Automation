from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
import time
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from pageObjects.SfHomePage import SalesForceHomePage
from selenium.common.exceptions import StaleElementReferenceException
from utilities.BaseClass import BaseClass



class TestOne(BaseClass):
    def test_e2e(self):
        log = self.getLogger()
        action = ActionChains(self.driver)
        wait = WebDriverWait(self.driver, 20)

        tabs = self.driver.window_handles
        self.driver.switch_to.window(tabs[1])
        sf_HomePage = SalesForceHomePage(self.driver)

        try:
            sf_HomePage.nav_console_home().click()
        except Exception as e:
            sf_HomePage.login().click()
            self.driver.get("https://optimatax--develop.lightning.force.com/lightning/page/home")
            log.info(e)
        try:
            sf_HomePage.create_data_button().click()
            log.info("In the Salesforce sales console, on the home page, selected 'create data'")
        except Exception as e:
            alert = self.driver.switch_to.alert()
            alert.accept()
            log.info(e)

        clientInformation = self.getTempEmail()
        self.driver.switch_to.window(tabs[1])
        sf_HomePage.create_data_email().send_keys(clientInformation["email_address"])
        sf_HomePage.create_data_name().send_keys(clientInformation["first_name"] + " " + clientInformation["last_name"])

        leadPage = sf_HomePage.create_data_submit()
        log.info("Filled out the required fields: Name Email set 'stage' drop-down field as 'lead' selected 'create data'")
        button = leadPage.phone_edit_pencil()
        self.driver.execute_script("arguments[0].click();", button)


        tel_css_selector = leadPage.phone_number().get_attribute("value")
        leadPage.phone_number().clear()
        save = leadPage.contact_details_save()
        self.driver.execute_script("arguments[0].click();", save)
        log.info("Deleted primary phone field from the created lead and selected 'save'")

        # Checking visibility means the element is displayed returns the WebElement
        self.checkVisibility(leadPage.conversionReadinessPhone)
        #wait.until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, "h3[title='Phone']")))
        log.info("Under 'lead conversion readiness' window–'convert' button is not visible and shows phone"
                 " field that needs to be entered in order to convert")
        self.driver.execute_script("window.scrollTo(0,0);")

        time.sleep(1)
        self.driver.refresh()

        #checkPresence will return WebElement
        edit_pencil = self.checkPresence(leadPage.primaryPhoneEditPencil)
        self.driver.execute_script("arguments[0].click();", edit_pencil)
        self.driver.execute_script("window.scrollTo(0,0);")

        leadPage.phone_number().send_keys(tel_css_selector)
        secondSave = leadPage.contact_details_save()
        action.move_to_element(secondSave).perform()
        action.click(secondSave).perform()
        log.info("Entered all required fields and selected 'save'")


        convertButton = leadPage.convert_button()
        self.driver.execute_script("arguments[0].click();", convertButton)
        log.info("Selected 'convert' in 'lead conversion readiness' window")

        invOpportunity = leadPage.lead_conversion_save()
        log.info("Select 'save' in 'lead conversion' modal")
        #presence works because it only checks if element is on DOM vs visibility which checks both–visibility and DOM
        self.checkPresence(invOpportunity.paymentScheduleButton)
        time.sleep(5)
        self.driver.refresh()

        # checkPresence will return WebElement and check presence
        payment_schedule_button = self.checkPresence(invOpportunity.paymentScheduleButton)
        self.driver.execute_script("arguments[0].click();", payment_schedule_button)
        log.info("In the investigation opportunity, selected 'create payment schedules'")

        try:
            self.selectDate()
            invOpportunity.iframe_payment_save_button().click()
            self.driver.switch_to.default_content()
            log.info("Selected payment date <= 30 days and selected 'save'")
            self.checkInvisibility(invOpportunity.paymentModuleHeader)
        except:
            log.warning("A modal appeared with no fields so will refresh and try again")
            self.driver.refresh()
            log.info("Refreshed successfully")
            # checkPresence will return WebElement and check presence
            payment_schedule_button = self.checkPresence(invOpportunity.paymentScheduleButton)
            self.driver.execute_script("arguments[0].click();", payment_schedule_button)
            log.warning("In the investigation opportunity, selected 'create payment schedules'")
            self.selectDate()
            invOpportunity.iframe_payment_save_button().click()
            self.driver.switch_to.default_content()
            log.info("Selected payment date <= 30 days and selected 'save'")
            self.checkInvisibility(invOpportunity.paymentModuleHeader)

        # element is either a locator (text) or an WebElement
        self.checkClickablity(invOpportunity.manage_docs_tab())
        manage_docs_element = invOpportunity.manage_docs_tab()
        self.driver.execute_script("arguments[0].click();", manage_docs_element)

        self.checkFrameAndSwitchToIt(invOpportunity.manageDocsIframeOne)
        self.checkFrameAndSwitchToIt(invOpportunity.manageDocsIframeTwo)
        self.checkClickablity(invOpportunity.manageDocsStart)
        invOpportunity.manage_docs_start().click()
        self.checkClickablity(invOpportunity.sendEmail)
        disposableEmail = invOpportunity.send_email()
        tabs = self.driver.window_handles
        self.driver.switch_to.window(tabs[2])

        self.driver.switch_to.default_content()
        disposableEmail.welcome_email().click()
        self.driver.switch_to.frame("iframeMail")
        portalPasswordCreate = disposableEmail.welcome_email_create_link()
        time.sleep(1)


        portal = self.driver.window_handles[3]
        self.driver.switch_to.window(portal)
        portalPasswordCreate.portal_password().send_keys("123456")
        portalPasswordCreate.confirm_password().send_keys("123456")
        self.driver.find_element(By.CSS_SELECTOR, "button[id='login-btn'").click()
        self.driver.find_element(By.XPATH, "//button[contains(text(), 'Acknowledge')]").click()
        #wait.until(expected_conditions.visibility_of_element_located((By.XPATH, "//button[contains(text(), 'Started')]")))

        try:
            self.checkClickablity((By.XPATH, "//button[contains(text(), 'Started')]"))
            self.driver.find_element(By.XPATH, "//button[contains(text(), 'Started')]").click()
        except StaleElementReferenceException as Exception:
            print('StaleElementReferenceException while trying to click start, trying to find element again')
            self.checkClickablity((By.XPATH, "//button[contains(text(), 'Started')]"))
            self.driver.find_element(By.XPATH, "//button[contains(text(), 'Started')]").click()

        self.checkClickablity((By.LINK_TEXT, "I Agree"))
        self.driver.find_element(By.LINK_TEXT, "I Agree").click()

        canvas = self.driver.find_element(By.CSS_SELECTOR, "div[class*='pad--body'] canvas")
        action.click_and_hold(canvas) \
            .move_by_offset(-10, -15) \
            .move_by_offset(20, 32) \
            .move_by_offset(10, 25) \
            .release()
        action.perform()
        submit_button = self.driver.find_element(By.XPATH, "//button[contains(text(),'Submit')]")
        self.driver.execute_script("arguments[0].click();", submit_button)

        ssn = self.driver.find_element(By.CSS_SELECTOR, "input[name='masked_tax_identification_number']")
        ssn.send_keys("123456789")
        dob_dropdowns_elements = self.driver.find_elements(By.CSS_SELECTOR, "select[name*='birth']")
        for dob in dob_dropdowns_elements:
            date_select = Select(dob)
            date_select.select_by_index(2)
        self.checkVisibility((By.CSS_SELECTOR, "button[id='show-confirmation-modal']"))
        verify_button = self.driver.find_element(By.CSS_SELECTOR, "button[id='show-confirmation-modal']")
        self.driver.execute_script("arguments[0].click();", verify_button)
        self.driver.find_element(By.CSS_SELECTOR,"button[id='forms-nav-verify']").click()

        for i in range(4):
            try:
                self.driver.find_element(By.PARTIAL_LINK_TEXT, "View").click()
                self.driver.find_element(By.LINK_TEXT, "read more...").click()
                program_outline = self.driver.find_elements(By.CSS_SELECTOR, "div[class='more'] p")
                for p in program_outline:
                    text = p.text
                    assert text is not None, "Program outline may be missing contents please login to check."
                self.driver.find_element(By.CSS_SELECTOR, "button[class='close']").click()
                # self.driver.execute_script("argument[0].scrollIntoView();", close_element)
                # close_element.click()
                continue_button_location = self.driver.find_element(By.CSS_SELECTOR, "[class*='btn-success']")
                self.driver.execute_script("arguments[0].click();", continue_button_location)
            except:
                self.driver.find_element(By.CSS_SELECTOR, "button[class='close']").click()
                continue_button_location = self.driver.find_element(By.CSS_SELECTOR, "[class*='btn-success']")
                self.driver.execute_script("arguments[0].click();", continue_button_location)

        self.driver.find_element(By.XPATH, "//div[@id='signers']/button[1]").click()

        self.driver.find_element(By.XPATH, "//button[contains(text(),'Credit or Debit Card')]").click()

        self.driver.find_element(By.CSS_SELECTOR, "input[id='cc-number']").send_keys("4111111111111111")

        self.driver.find_element(By.CSS_SELECTOR, "input[name='cc_cvv']").send_keys("123")

        #check confirm payment schedule button because it goes back to the payment page
        for i in range(4):

            continue_button_location = self.driver.find_element(By.CSS_SELECTOR, "[class*='btn-success']")
            self.driver.execute_script("arguments[0].click();", continue_button_location)

        self.driver.switch_to.window(tabs[1])
        self.driver.refresh()

        wait.until(expected_conditions.element_to_be_clickable((By.XPATH, "//ul[@role='tablist']/li[7]/a")))
        manage_docs_element = self.driver.find_element(By.XPATH, "//ul[@role='tablist']/li[7]/a")
        #elf.driver.execute_script("arguments[0].click();", manage_docs_element)

        wait.until(expected_conditions.frame_to_be_available_and_switch_to_it(
            (By.XPATH, "//div[@class='content iframe-parent']/iframe")))
        # putting sleep here because error that iframe cannot be found is thrown
        time.sleep(1)
        wait.until(
            expected_conditions.frame_to_be_available_and_switch_to_it((By.XPATH, "//iframe[@id='manage-forms']")))
        time.sleep(2)
        self.driver.find_element(By.CSS_SELECTOR, "button[id='ready-for-payments-btn']").click()

        self.driver.execute_script("window.open('about:blank','admin_portal');")
        self.driver.switch_to.window("admin_portal")
        self.driver.get("https://admin-dev.optimatax.com/dashboard")

        self.driver.find_element(By.CSS_SELECTOR, "input[id='search']").send_keys(clientInformation["first_name"])
        self.driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
        self.driver.find_element(By.PARTIAL_LINK_TEXT,"Opportunities").click()
        self.driver.find_element(By.PARTIAL_LINK_TEXT, "Opportunity").click()
        self.driver.find_element(By.XPATH, "//tr[@id='form-21244']/td[5]").click()
        self.driver.find_element(By.PARTIAL_LINK_TEXT, "Approve").click()
        self.driver.find_element(By.PARTIAL_LINK_TEXT, "Services").click()
        self.driver.find_element(By.PARTIAL_LINK_TEXT, "Payments").click()
        self.driver.find_element(By.PARTIAL_LINK_TEXT, "Payment Schedule").click()
        self.driver.find_element(By.XPATH, "//button[contains(text(),'Pay Now')]").click()
        self.driver.find_element(By.CSS_SELECTOR, "button[data-form-id='pay-now-otr-form']").click()

        try:
            alert_success_element = self.driver.find_element(By.XPATH, "//div[contains(text(), 'processed successfully.')]")
            wait.until(expected_conditions.visibility_of(alert_success_element))
            print(alert_success_element.text)
        except:
            print("Unable to verify alert-success for Payment")

        self.driver.switch_to.window(tabs[1])





























