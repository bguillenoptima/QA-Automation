import pytest
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
import time

from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

from pageObjects.SfHomePage import SalesForceHomePage
from pageObjects.SfInvOpportunity import SalesForceInvOpportunityPage
from utilities.BaseClass import BaseClass
import datetime


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
        except Exception as e:
            alert = self.driver.switch_to.alert()
            alert.accept()
            log.info(e)

        clientInformation = self.getTempEmail()
        self.driver.switch_to.window(tabs[1])
        sf_HomePage.create_data_email().send_keys(clientInformation["email_address"])
        sf_HomePage.create_data_name().send_keys(clientInformation["first_name"] + " " + clientInformation["last_name"])

        leadPage = sf_HomePage.create_data_submit()
        button = leadPage.phone_edit_pencil()
        self.driver.execute_script("arguments[0].click();", button)

        tel_css_selector = leadPage.phone_number().get_attribute("value")
        leadPage.phone_number().clear()
        save = leadPage.contact_details_save()
        self.driver.execute_script("arguments[0].click();", save)

        wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, "h3[title='Phone']")))
        time.sleep(2)
        phone_lead_conversion_window = leadPage.conversion_readiness_phone().text
        self.driver.execute_script("window.scrollTo(0,0);")
        assert "Phone" in phone_lead_conversion_window
        time.sleep(1)
        self.driver.refresh()

        wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, "button[title='Edit Phone, Primary'] lightning-primitive-icon")))
        edit_pencil = leadPage.phone_edit_pencil()
        self.driver.execute_script("arguments[0].click();", edit_pencil)
        self.driver.execute_script("window.scrollTo(0,0);")

        leadPage.phone_number().send_keys(tel_css_selector)
        secondSave = leadPage.contact_details_save()
        action.move_to_element(secondSave).perform()
        action.click(secondSave).perform()


        convertButton = leadPage.convert_button()
        self.driver.execute_script("arguments[0].click();", convertButton)

        invOpportunity = leadPage.lead_conversion_save()
        wait.until(expected_conditions.presence_of_element_located((By.XPATH, "//button[contains(text(), 'Create Pmt Schedules')]")))
        self.driver.refresh()
        wait.until(expected_conditions.presence_of_element_located((By.XPATH, "//button[contains(text(), 'Create Pmt Schedules')]")))
        payment_schedule_button = invOpportunity.payment_schedule_button()
        self.driver.execute_script("arguments[0].click();", payment_schedule_button)

        time.sleep(5)
        try:
            self.selectDate()
            invOpportunity.iframe_payment_save_button().click()
            self.driver.switch_to.default_content()
            wait.until(expected_conditions.invisibility_of_element((By.XPATH, "//h2[contains(text(), 'Create Payment Schedule')]")))
        except:
            self.driver.refresh()
            wait.until(expected_conditions.presence_of_element_located((By.XPATH, "//button[contains(text(), 'Create Pmt Schedules')]")))
            self.driver.execute_script("arguments[0].click();", payment_schedule_button)
            wait.until(expected_conditions.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR, "div[id='modal-content-id-1'] iframe")))
            wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, "input[type='date']")))
            invOpportunity.iframe_payment_save_button().click()


        wait.until(expected_conditions.element_to_be_clickable((By.XPATH, "//ul[@role='tablist']/li[7]/a")))
        manage_docs_element = invOpportunity.manage_docs_tab()
        self.driver.execute_script("arguments[0].click();", manage_docs_element)

        wait.until(expected_conditions.frame_to_be_available_and_switch_to_it((By.XPATH, "//div[@class='content iframe-parent']/iframe")))
        #putting sleep here because error that iframe cannot be found is thrown
        time.sleep(1)
        wait.until(expected_conditions.frame_to_be_available_and_switch_to_it((By.XPATH, "//iframe[@id='manage-forms']")))
        time.sleep(2)
        self.driver.find_element(By.CSS_SELECTOR, "i[class ='fa fa-rocket']").click()
        wait.until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, "button[class='btn btn-success send-email']")))
        self.driver.find_element(By.CSS_SELECTOR, "button[class='btn btn-success send-email']").click()
        tabs = self.driver.window_handles
        self.driver.switch_to.window(tabs[2])
        self.driver.find_element(By.CSS_SELECTOR, "a[title='Refresh this page']").click()

        self.driver.switch_to.default_content()
        self.driver.find_element(By.XPATH, "//td[contains(text(),'Welcome to Optima Tax Relief')]").click()
        self.driver.switch_to.frame("iframeMail")
        self.driver.find_element(By.LINK_TEXT, "Create Account →").click()
        time.sleep(1)


        portal = self.driver.window_handles[3]
        self.driver.switch_to.window(portal)
        self.driver.find_element_by_name("password").send_keys("123456")
        self.driver.find_element_by_name("password_confirmation").send_keys("123456")
        self.driver.find_element(By.CSS_SELECTOR, "button[id='login-btn'").click()
        self.driver.find_element(By.XPATH, "//button[contains(text(), 'Acknowledge')]").click()
        self.driver.find_element(By.XPATH, "//button[contains(text(), 'Started')]").click()
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

        self.driver.find_element(By.CSS_SELECTOR, "input[id='cc-number']").send_keys(self.PagesData.pagesData["credit_card_number"])

        self.driver.find_element(By.CSS_SELECTOR, "input[name='cc_cvv']").send_keys(self.PagesData.pagesData["client_ssn"])

        #check confirm payment schedule button because it goes back to the payment page
        for i in range(4):

            continue_button_location = self.driver.find_element(By.CSS_SELECTOR, "[class*='btn-success']")
            self.driver.execute_script("arguments[0].click();", continue_button_location)

        self.driver.switch_to.window(sf_window)
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

        self.driver.switch_to.window(sf_window)





























