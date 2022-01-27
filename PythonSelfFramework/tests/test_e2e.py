from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
import time

from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from utilities.BaseClass import BaseClass
import datetime
from selenium.webdriver.common.keys import Keys


class TestOne(BaseClass):

    def test_e2e(self):
        action = ActionChains(self.driver)
        wait = WebDriverWait(self.driver, 20)

        sf_window = self.driver.window_handles[1]
        self.driver.switch_to.window(sf_window)
        try:
            self.driver.find_element(By.LINK_TEXT, "Office 365").click()
            self.driver.get("https://optimatax--develop.lightning.force.com/lightning/page/home")

        except Exception as e:
            self.driver.get("https://optimatax--develop.lightning.force.com/lightning/page/home")
            print(e)
        try:
            alert = self.driver.switch_to.alert()
            alert.accept()
        except Exception as e:
            print(e)

        self.driver.find_element(By.XPATH, "//div[@class='slds-card__body']/button").click()

        self.driver.execute_script("window.open('about:blank','disposable_email');")
        self.driver.switch_to.window("disposable_email")
        self.driver.get("https://www.disposablemail.com/")
        email = self.driver.find_element(By.CSS_SELECTOR, "span[id='email']").text

        self.driver.switch_to.window(sf_window)
        self.driver.find_element(By.XPATH, "//div[@id='modal-content-id-1']/div[6]/input").send_keys(email)

        first_name_last_name = email.split(".")
        firstName = first_name_last_name[0].capitalize()
        parsedLastname = first_name_last_name[1].split("@")
        lastName = parsedLastname[1].capitalize()

        self.driver.find_element(By.XPATH, "//div[@id='modal-content-id-1']/div[1]/input").send_keys(firstName + " " + lastName)
        self.driver.find_element(By.CSS_SELECTOR, "button[title='Create Data']").click()

        button = self.driver.find_element_by_xpath("//button[@title='Edit Phone, Primary']/lightning-primitive-icon")
        self.driver.execute_script("arguments[0].click();", button)

        tel_css_selector = self.driver.find_element(By.XPATH, "//a[contains(text(), 'Contact Details')]/parent::h2/parent::div/parent::div/parent::div/parent::div/div[2]/div/div/div[2]/div/section/div[2]/div/div[1]/div/div/div/div/div[2]/div[1]/div/div/div/input").get_attribute(
            "value")

        self.driver.find_element(By.XPATH, "//a[contains(text(), 'Contact Details')]/parent::h2/parent::div/parent::div/parent::div/parent::div/div[2]/div/div/div[2]/div/section/div[2]/div/div[1]/div/div/div/div/div[2]/div[1]/div/div/div/input").clear()
        save = self.driver.find_element_by_xpath("//button[@title='Save']")
        self.driver.execute_script("arguments[0].click();", save)

        wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, "h3[title='Phone']")))
        phone_lead_conversion_window = self.driver.find_element(By.CSS_SELECTOR, "h3[title='Phone']").text
        self.driver.execute_script("window.scrollTo(0,0);")
        assert "Phone" in phone_lead_conversion_window
        time.sleep(1)
        self.driver.refresh()

        #adding wait because execute script of clicking the edit penchil is happening before the pencil is loaded.
        wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, "button[title='Edit Phone, Primary'] lightning-primitive-icon")))
        edit_pencil = self.driver.find_element(By.XPATH,"//button[@title='Edit Phone, Primary']/lightning-primitive-icon")
        self.driver.execute_script("arguments[0].click();", edit_pencil)
        self.driver.execute_script("window.scrollTo(0,0);")
        self.driver.find_element(By.XPATH,"//a[contains(text(), 'Contact Details')]/parent::h2/parent::div/parent::div/parent::div/parent::div/div[2]/div/div/div[2]/div/section/div[2]/div/div[1]/div/div/div/div/div[2]/div[1]/div/div/div/input").send_keys(tel_css_selector)
        second_save = self.driver.find_element(By.XPATH, "//span[contains(text(),'Save' )]")
        action.move_to_element(second_save).perform()
        action.click(second_save).perform()


        convert_button = self.driver.find_element(By.XPATH, "//button[contains(text(),'Convert')]")
        self.driver.execute_script("arguments[0].click();", convert_button)

        java_button = self.driver.find_element(By.XPATH, "//button[contains(text(),'Save')]")
        self.driver.execute_script("arguments[0].click();", java_button)

        wait.until(expected_conditions.presence_of_element_located((By.XPATH, "//button[contains(text(), 'Create Pmt Schedules')]")))
        self.driver.refresh()
        wait.until(expected_conditions.presence_of_element_located((By.XPATH, "//button[contains(text(), 'Create Pmt Schedules')]")))
        time.sleep(2)
        create_payment_schedule_button = self.driver.find_element(By.XPATH, "//button[contains(text(), 'Create Pmt Schedules')]")
        self.driver.execute_script("arguments[0].click();", create_payment_schedule_button)

        wait.until(expected_conditions.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR, "div[id='modal-content-id-1'] iframe")))
        date_element = self.driver.find_element(By.CSS_SELECTOR, "input[type='date']")
        #current_time = datetime.datetime.now()
        #date = str(current_time.strftime(("%m"))) + str(current_time.day) + str(current_time.year)

        action.move_to_element(date_element).perform()
        action.click(date_element).perform()
        action.send_keys(Keys.ARROW_UP).send_keys(Keys.ARROW_LEFT).perform()
        action.send_keys(Keys.ARROW_DOWN).send_keys(Keys.ARROW_LEFT).perform()
        action.send_keys(Keys.ARROW_UP).perform()
        self.driver.find_element(By.CSS_SELECTOR, "input[type = 'submit']").click()
        time.sleep(10)

        self.driver.switch_to.default_content()
        wait.until(expected_conditions.element_to_be_clickable((By.XPATH, "//ul[@role='tablist']/li[7]/a")))
        manage_docs_element = self.driver.find_element(By.XPATH, "//ul[@role='tablist']/li[7]/a")
        self.driver.execute_script("arguments[0].click();", manage_docs_element)

        wait.until(expected_conditions.frame_to_be_available_and_switch_to_it((By.XPATH, "//div[@class='content iframe-parent']/iframe")))
        #putting sleep here because error that iframe cannot be found is thrown
        time.sleep(1)
        wait.until(expected_conditions.frame_to_be_available_and_switch_to_it((By.XPATH, "//iframe[@id='manage-forms']")))
        rocket = self.driver.find_element(By.CSS_SELECTOR, "i[class ='fa fa-rocket']")
        send_email = self.driver.find_element(By.CSS_SELECTOR, "button[class='btn btn-success send-email']")
        action.click(rocket).perform()
        action.click(send_email).perform()
        self.driver.switch_to.window("disposable_email")
        self.driver.find_element(By.CSS_SELECTOR, "a[title='Refresh this page']").click()

        self.driver.switch_to.default_content()
        self.driver.find_element(By.XPATH, "//td[contains(text(),'Welcome to Optima Tax Relief')]").click()
        self.driver.switch_to.frame("iframeMail")
        self.driver.find_element(By.LINK_TEXT, "Create Account →").click()

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



















