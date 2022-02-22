from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
import time
from selenium.webdriver.support.wait import WebDriverWait

from pageObjects.O365LoginPages import O365LoginPages
from selenium.common.exceptions import StaleElementReferenceException
from utilities.BaseClass import BaseClass
from pageObjects.TaxInformationPage import TaxInformationAuthorization



class TestOne(BaseClass):
    def test_e2e(self):
        log = self.getLogger()
        action = ActionChains(self.driver)
        wait = WebDriverWait(self.driver, 20)

        sfLoginPage = O365LoginPages(self.driver)
        sf_HomePage = sfLoginPage.office_365_button()
        tabs = self.driver.window_handles
        sfTab = tabs[len(tabs) - 1]

        try:
            sf_HomePage.create_data_button().click()
            log.info("In the Salesforce sales console, on the home page, selected 'create data'")
        except Exception as e:
            alert = self.driver.switch_to.alert()
            alert.accept()
            log.info(e)

        clientInformation = self.getTempEmail()
        tabs = self.driver.window_handles
        disposableEmailTab = tabs[len(tabs) - 1]
        self.driver.switch_to.window(sfTab)
        sf_HomePage.create_data_email().send_keys(clientInformation["email_address"])
        sf_HomePage.create_data_name().send_keys(clientInformation["first_name"] + " " + clientInformation["last_name"])

        leadPage = sf_HomePage.create_data_submit()
        log.info(
            "Filled out the required fields: Name Email set 'stage' drop-down field as 'lead' selected 'create data'")
        edit_pencil = leadPage.phone_edit_pencil()
        self.driver.execute_script("arguments[0].click();", edit_pencil)

        tel_css_selector = leadPage.phone_number().get_attribute("value")
        leadPage.phone_number().clear()
        save = leadPage.contact_details_save()
        self.driver.execute_script("arguments[0].click();", save)
        log.info("Deleted primary phone field from the created lead and selected 'save'")

        # Checking visibility means the element is displayed returns the WebElement
        wait.until(expected_conditions.text_to_be_present_in_element(leadPage.conversionReadinessPhone, "Phone"))
        self.driver.execute_script("window.scrollTo(0,0);")
#        self.checkVisibility(leadPage.conversionReadinessPhone)
        log.info("Under 'lead conversion readiness' window–'convert' button is not visible and shows phone"
                 " field that needs to be entered in order to convert")

        time.sleep(1)
        self.driver.refresh()
        wait.until(expected_conditions.staleness_of(edit_pencil))

        # checkPresence will return WebElement
        self.driver.execute_script("window.scrollTo(0,0);")
        edit_pencil = self.checkPresence(leadPage.primaryPhoneEditPencil)

        try:
            self.driver.execute_script("arguments[0].click();", edit_pencil)
            self.driver.execute_script("window.scrollTo(0,0);")
        except StaleElementReferenceException as Exception:
            editPencil = leadPage.phone_edit_pencil()
            self.driver.execute_script("arguments[0].click();", editPencil)
            log.warning(Exception)

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
        # presence works because it only checks if element is on DOM vs visibility which checks both–visibility and DOM
        payment_schedule_button = self.checkPresence(invOpportunity.paymentScheduleButton)
        time.sleep(5)
        self.driver.refresh()

        try:
            wait.until(expected_conditions.staleness_of(payment_schedule_button))
            time.sleep(10)
            payment_schedule_button = self.checkPresence(invOpportunity.paymentScheduleButton)
            self.driver.execute_script("arguments[0].click();", payment_schedule_button)
            time.sleep(5)
            log.info("In the investigation opportunity, selected 'create payment schedules'")
        except StaleElementReferenceException as Exception:
            log.warning(Exception)
            paymentScheduleButton = invOpportunity.payment_schedule_button()
            self.driver.execute_script("arguments[0].click();", paymentScheduleButton)
            log.info("In the investigation opportunity, selected 'create payment schedules'")

        # checkPresence will return WebElement and check presence
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
            wait.until(expected_conditions.staleness_of(payment_schedule_button))

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

        action.click(invOpportunity.manage_docs_start()).perform()
        self.checkClickablity(invOpportunity.sendEmail)

        disposableEmail = invOpportunity.send_email()

        self.driver.switch_to.window(disposableEmailTab)

        self.driver.switch_to.default_content()
        disposableEmail.welcome_email().click()
        self.driver.switch_to.frame("iframeMail")

        portalPasswordCreate = disposableEmail.welcome_email_create_link()

        tabs = self.driver.window_handles
        portal = tabs[len(tabs) - 1]
        self.driver.switch_to.window(portal)
        portalPasswordCreate.portal_password().send_keys(self.parameters["client_password"])
        portalPasswordCreate.confirm_password().send_keys(self.parameters["client_password"])
        portalHomepage = portalPasswordCreate.create_account()

        self.checkClickablity(portalHomepage.acknowledge)
        portalHomepage.portal_acknowledge().click()

        try:
            self.checkClickablity(portalHomepage.getStarted)
            portalHomepage.portal_get_started().click()
        except StaleElementReferenceException as Exception:
            log.info('StaleElementReferenceException while trying to click start, trying to find element again')
            self.checkClickablity(portalHomepage.getStarted)
            portalHomepage.portal_get_started().click()
            log.info(Exception)

        self.checkClickablity(portalHomepage.agree)
        signaturePage = portalHomepage.portal_agree()

        canvas = signaturePage.portal_canvas()
        self.sign(canvas)
        infoVerificationPage = signaturePage.portal_submit()

        infoVerificationPage.ssn_field().send_keys(self.parameters["client_ssn"])
        dateOfBirthDropDowns = infoVerificationPage.dob_drop_downs()
        self.enter_dob(dateOfBirthDropDowns)
        self.checkVisibility(infoVerificationPage.verify)

        verifyButton = infoVerificationPage.verify_button()
        self.driver.execute_script("arguments[0].click();", verifyButton)
        serviceAgreementPage = infoVerificationPage.confirm_button()

        for serviceAgreement in range(2):
            serviceAgreementPage.view_form_button().click()
            serviceAgreementPage.read_more_button().click()
            self.check_paragraph_contents(serviceAgreementPage.content())
            serviceAgreementPage.x_button().click()
            continue_button_location = serviceAgreementPage.continue_button()
            self.driver.execute_script("arguments[0].click();", continue_button_location)

        taxInformation = TaxInformationAuthorization(self.driver)
        taxInformation.view_form().click()
        self.check_image_visibility(taxInformation.form_image())
        taxInformation.x_button().click()
        requestForTranscript = taxInformation.continue_button()

        transcriptsViewLinks = requestForTranscript.view_form_elements()
        for viewLink in transcriptsViewLinks:
            viewLink.click()
            self.check_image_visibility(requestForTranscript.form_image())
            requestForTranscript.x_button().click()
        paymentAuthPages = requestForTranscript.continue_button()

        paymentAuthPages.payment_signer().click()
        paymentAuthPages.card_button().click()
        paymentAuthPages.card_number_field().send_keys(
            self.parameters["credit_card_number"])
        paymentAuthPages.cvv_number_field().send_keys(self.parameters["cvv"])

        for i in range(2):
            paymentAuthPages.continue_button().click()
        paymentAuthPages.confirm_schedule_button().click()
        paymentAuthPages.apply_signature_button().click()


        self.driver.switch_to.window(sfTab)
        self.driver.refresh()

        self.checkClickablity(invOpportunity.manageDocsTab)
        invOpportunity.manage_docs_tab().click()

        self.checkFrameAndSwitchToIt(invOpportunity.manageDocsIframeOne)
        self.checkFrameAndSwitchToIt(invOpportunity.manageDocsIframeTwo)
        invOpportunity.payments_ready().click()

        if self.env_name == "dev":
            tabs = self.openTab("admin_portal", "https://admin-dev.optimatax.com/dashboard")
        elif self.env_name == "staging":
            tabs = self.openTab("admin_portal", "https://admin-staging.optimatax.com/dashboard")
        elif self.env_name == "prod":
            self.driver.get("https://admin.optimatax.com/dashboard")


        adminPortal = tabs[len(tabs) - 1]

        self.driver.switch_to.window(adminPortal)


        self.driver.find_element(By.CSS_SELECTOR, "input[id='search']").send_keys(clientInformation["first_name"])
        self.driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
        self.driver.find_element(By.PARTIAL_LINK_TEXT, "Opportunities").click()
        self.driver.find_element(By.PARTIAL_LINK_TEXT, "Opportunity").click()
        self.driver.find_element(By.XPATH, "//div[@id='forms-tab']/div[2]/table/tbody/tr[9]/td[5]").click()
        self.driver.find_element(By.PARTIAL_LINK_TEXT, "Approve").click()
        self.driver.find_element(By.PARTIAL_LINK_TEXT, "Services").click()
        self.driver.find_element(By.PARTIAL_LINK_TEXT, "Payments").click()
        self.driver.find_element(By.PARTIAL_LINK_TEXT, "Payment Schedule").click()
        self.driver.find_element(By.XPATH, "//button[contains(text(),'Pay Now')]").click()
        payNow = self.driver.find_element(By.CSS_SELECTOR, "button[data-form-id='pay-now-otr-form']")
        self.driver.execute_script("arguments[0].click();", payNow)

        try:
            alert_success_element = self.driver.find_element(By.XPATH, "//div[contains(text(), 'processed successfully.')]")
            wait.until(expected_conditions.visibility_of(alert_success_element))
            print(alert_success_element.text)
        except:
            print("Unable to verify alert-success for Payment")

