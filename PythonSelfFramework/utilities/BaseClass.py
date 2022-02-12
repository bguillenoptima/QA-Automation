import datetime
import time

import pytest
import logging
import inspect

from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC, wait, expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from pageObjects.DisposableEmailPage import DisposableEmailPage
logger = logging.getLogger(__name__)

fileHandler = logging.FileHandler('logfile.log')

logger.addHandler(fileHandler)  #filehandler object

@pytest.mark.usefixtures("setup", "dataLoad")
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

    #An expectation for checking that an element is present on the DOM
    #of a page. This does not necessarily mean that the element is visible.
    #locator - used to find the element (by, path)
    #returns the WebElement once it is located
    def checkPresence(self, locator):
        element = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((locator)))
        return element

    def checkFrameAndSwitchToIt(self, locator):
        element = WebDriverWait(self.driver, 20).until(EC.frame_to_be_available_and_switch_to_it((locator)))
        return element

    def verifyCSSPresence(self,text):
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((text)))

    def verifyPresence(self, locator, syntax):
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((locator, syntax)))

    def verifyLinkPresence(self, text):
        element = WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located((By.LINK_TEXT, text)))

    def verifyVisibilityOf(self, locator, text):
        WebDriverWait(self.driver, 20).until(EC.visibility_of((locator, text)))

    def openTab(self, tabName, URI):
        self.driver.execute_script("window.open('about:blank','arguments[0]');", tabName)
        tabs = self.driver.window_handles
        tabs_count = len(tabs) - 1
        self.driver.switch_to.window(tabs[tabs_count])
        self.driver.get(URI)

    def getTempEmail(self):
        self.openTab("disposable_email","https://www.disposablemail.com/")
        emailInbox = DisposableEmailPage(self.driver)
        email_Address = emailInbox.store_email().text
        first_name_last_name = email_Address.split(".")
        first_Name = first_name_last_name[0].capitalize()
        parsedLastname = first_name_last_name[1].split("@")
        last_Name = parsedLastname[0].capitalize()

        firstName = first_Name
        lastName = last_Name
        email = email_Address
        clientData = dict(first_name=firstName, last_name=lastName, email_address=email)
        return clientData

    def getDate(self):
        current_time = datetime.datetime.now()
        date = str(current_time.strftime(("%m"))) + str(current_time.day) + str(current_time.year)
        return date

    def selectDate(self):
        #wait = WebDriverWait(self.driver, 20)
        current_time = datetime.datetime.now()
        day = int(current_time.day)
        month = int(current_time.strftime(("%m")))
        #date = str(current_time.strftime(("%m"))) + str(current_time.day) + str(current_time.year)

        self.checkFrameAndSwitchToIt((By.CSS_SELECTOR, "div[id='modal-content-id-1'] iframe"))
        date_element = self.checkPresence((By.CSS_SELECTOR, "input[type='date']"))
        #wait.until(expected_conditions.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR, "div[id='modal-content-id-1'] iframe")))
        #wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, "input[type='date']")))
        #date_element = self.driver.find_element(By.CSS_SELECTOR, "input[type='date']")
        action = ActionChains(self.driver)
        action.move_to_element(date_element).perform()
        action.click(date_element).perform()
        action.send_keys(Keys.ARROW_UP).send_keys(Keys.ARROW_LEFT).perform()
        for uparrow in range(day):
            action.send_keys(Keys.ARROW_UP).perform()
        action.send_keys(Keys.ARROW_LEFT).perform()

        for uparrow in range(month):
            action.send_keys(Keys.ARROW_UP).perform()



