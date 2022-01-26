
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
import time
from selenium.webdriver.support.wait import WebDriverWait
from utilities.BaseClass import BaseClass
import datetime
from selenium.webdriver.common.keys import Keys


class TestOne(BaseClass):

    def test_e2e(self):
        wait = WebDriverWait(self.driver, 20)

        sf_window = self.driver.window_handles[1]
        self.driver.switch_to.window(sf_window)
        self.driver.get("https://optimatax--develop.lightning.force.com/lightning/page/home")

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


        wait.until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, "button[title='Edit Phone, Primary'] lightning-primitive-icon")))
        button = self.driver.find_element_by_xpath("//button[@title='Edit Phone, Primary']/lightning-primitive-icon")
        self.driver.execute_script("arguments[0].click();", button)

        wait.until(expected_conditions.presence_of_element_located((By.XPATH,"//a[contains(text(), 'Contact Details')]/parent::h2/parent::div/parent::div/parent::div/parent::div/div[2]/div/div/div[2]/div/section/div[2]/div/div[1]/div/div/div/div/div[2]/div[1]/div/div/div/input")))
        tel_css_selector = self.driver.find_element(By.XPATH, "//a[contains(text(), 'Contact Details')]/parent::h2/parent::div/parent::div/parent::div/parent::div/div[2]/div/div/div[2]/div/section/div[2]/div/div[1]/div/div/div/div/div[2]/div[1]/div/div/div/input").get_attribute(
            "value")
        print(tel_css_selector)

        self.driver.find_element(By.XPATH, "//a[contains(text(), 'Contact Details')]/parent::h2/parent::div/parent::div/parent::div/parent::div/div[2]/div/div/div[2]/div/section/div[2]/div/div[1]/div/div/div/div/div[2]/div[1]/div/div/div/input").clear()
        save = self.driver.find_element_by_xpath("//button[@title='Save']")
        self.driver.execute_script("arguments[0].click();", save)

        self.driver.execute_script("window.scrollTo(0,0);")
        phone_lead_conversion_window = self.driver.find_element(By.CSS_SELECTOR, "h3[title='Phone']").text
        assert "Phone" in phone_lead_conversion_window
        time.sleep(1)
        self.driver.refresh()

        wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, "button[title='Edit Phone, Primary'] lightning-primitive-icon")))
        edit_pencil = self.driver.find_element(By.XPATH,"//button[@title='Edit Phone, Primary']/lightning-primitive-icon")
        self.driver.execute_script("arguments[0].click();", edit_pencil)
        self.driver.find_element(By.XPATH,"//a[contains(text(), 'Contact Details')]/parent::h2/parent::div/parent::div/parent::div/parent::div/div[2]/div/div/div[2]/div/section/div[2]/div/div[1]/div/div/div/div/div[2]/div[1]/div/div/div/input").send_keys(tel_css_selector)
        second_save = self.driver.find_element(By.XPATH, "//span[contains(text(),'Save' )]")
        self.driver.execute_script("window.scrollTo(0,0);")
        self.driver.execute_script("arguments[0].click();", second_save)

        wait.until(expected_conditions.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Convert')]")))
        convert_button = self.driver.find_element(By.XPATH, "//button[contains(text(),'Convert')]")
        self.driver.execute_script("arguments[0].click();", convert_button)

        wait.until(expected_conditions.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Save')]")))
        java_button = self.driver.find_element(By.XPATH, "//button[contains(text(),'Save')]")
        self.driver.execute_script("arguments[0].click();", java_button)

        wait.until(expected_conditions.presence_of_element_located((By.XPATH, "//button[contains(text(), 'Create Pmt Schedules')]")))
        time.sleep(2)
        self.driver.refresh()
        wait.until(expected_conditions.presence_of_element_located((By.XPATH, "//button[contains(text(), 'Create Pmt Schedules')]")))
        create_payment_schedule_button = self.driver.find_element(By.XPATH, "//button[contains(text(), 'Create Pmt Schedules')]")
        self.driver.execute_script("arguments[0].click();", create_payment_schedule_button)

        wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, "div[id='modal-content-id-1'] iframe")))
        iframe = self.driver.find_element(By.CSS_SELECTOR, "div[id='modal-content-id-1'] iframe")
        self.driver.switch_to.frame(iframe)

        wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, "input[type='date']")))
        date_element = self.driver.find_element(By.CSS_SELECTOR, "input[type='date']")

        current_time = datetime.datetime.now()
        date = str(current_time.strftime(("%m"))) + str(current_time.day) + str(current_time.year)
        print(date)

        action = ActionChains(self.driver)
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
        iframe_three = self.driver.find_element(By.XPATH, "//iframe[@id='manage-forms']")
        self.driver.switch_to.frame(iframe_three)
        self.driver.find_element(By.CSS_SELECTOR, "i[class ='fa fa-rocket']").click()
        self.driver.find_element(By.CSS_SELECTOR, "button[class='btn btn-success send-email']").click()
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












