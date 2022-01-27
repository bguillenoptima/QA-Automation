from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time
from selenium.webdriver.common.keys import Keys


class TestOne:
    def test_e2e(self):
        driver.find_element(By.CSS_SELECTOR, "input[name='loginfmt']").send_keys("bguillen@optimataxrelief.com")
        driver.find_element(By.CSS_SELECTOR, "input[type='submit']").click()
        driver.find_element(By.CSS_SELECTOR, "input[type='password']").send_keys("Opti%6&8$")
        time.sleep(5)
        driver.find_element(By.XPATH, "//input[@type='submit']").click()
        # add twilio logic here
        time.sleep(10)
        driver.find_element(By.CSS_SELECTOR, "input[type='submit']").click()
        time.sleep(5)
        driver.find_element(By.CSS_SELECTOR, "input[type='submit']").click()
        driver.find_element(By.CSS_SELECTOR, "button[id='O365_MainLink_NavMenu']").click()
        driver.find_element(By.CSS_SELECTOR, "a[aria-label='Salesforce (Dev)']").click()
