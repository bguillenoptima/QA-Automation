import pytest
import logging
import inspect

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from pageObjects.DisposableEmailPage import DisposableEmailPage


@pytest.mark.usefixtures("setup")
class BaseClass:
    def getLogger(self):
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)
        fileHandler = logging.FileHandler('logfile.log')
        formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")
        fileHandler.setFormatter(formatter)

        logger.addHandler(fileHandler)  # filehandler object

        logger.setLevel(logging.DEBUG)
        return logger

    def verifyCSSPresence(self,text):
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, text)))

    def verifyLinkPresnce(self, text):
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.LINK_TEXT, text)))

    def verifyVisibilityOf(self, locator, text):
        WebDriverWait(self.driver, 20).until(EC.visibility_of((locator, text)))

    def homePageData(self):
        self.driver.execute_script("window.open('about:blank','disposable_email');")
        self.driver.switch_to.window("disposable_email")
        self.driver.get("https://www.disposablemail.com/")
        emailInbox = DisposableEmailPage(self.driver)
        email_Address = emailInbox.store_email().text
        first_name_last_name = email_Address.split(".")
        first_Name = first_name_last_name[0].capitalize()
        parsedLastname = first_name_last_name[1].split("@")
        last_Name = parsedLastname[0].capitalize()

        firstName = first_Name
        lastName = last_Name
        email = email_Address
        test_HomePage_data = dict(firstname=firstName, lastname=lastName, emailAddress=email)
        return test_HomePage_data

