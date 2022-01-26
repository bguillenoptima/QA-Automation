from selenium.webdriver.common.by import By
from pageObjects.CreateDataFormPage import CreateDataPage
from utilities.BaseClass import BaseClass


class TestCreateDataPage(BaseClass):

    def test_form_submission(self):
        create_data_form = CreateDataPage(self.driver)
        sf_window = self.driver.window_handles[1]
        self.driver.switch_to.window(sf_window)
        create_data_form.create_data_button().click()
        self.driver.execute_script("window.open('about:blank','disposable_email');")
        self.driver.switch_to.window("disposable_email")
        self.driver.get("https://www.disposablemail.com/")
        self.driver.find_element(By.LINK_TEXT, "Copy").click()
        email = self.driver.find_element(By.CSS_SELECTOR, "span[id='email']").text
        print(email)
        self.driver.switch_to.window(sf_window)
        create_data_form.email_field().send_keys(email)
        first_name_last_name = email.split(".")
        firstName = first_name_last_name[0].capitalize()
        parsedLastname = first_name_last_name[1].split("@")
        lastName = parsedLastname[1].capitalize()
        create_data_form.name_field_location().send_keys(firstName + " " + lastName)
        create_data_form.create_data_button_in_form().click()