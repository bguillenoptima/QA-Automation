from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time
from selenium.webdriver.common.keys import Keys

#browser exposes an executable file
#through selenium we need to invoke exe file which will then invok actual browser
#driver = webdriver.Firefox(executable_path="C:\\geckodriver.exe")
#driver = webdriver.Edge(executable_path="C:\\msedgedriver.exe")
driver = webdriver.Chrome("C:\\chromedriver.exe")
driver.implicitly_wait(5)
#driver.get("https://optimatax--staging.my.salesforce.com/")
#driver.find_element(By.CSS_SELECTOR, "input[type='email']").send_keys("bguillen@optimataxrelief.com.staging")
#driver.find_element(By.CSS_SELECTOR, "input[type='password']").send_keys("Opti%6&8$")
#driver.find_element(By.CSS_SELECTOR, "input[type='submit']").click()
#driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.get("https://portal.office365.com")
driver.find_element(By.CSS_SELECTOR, "input[name='loginfmt']").send_keys("bguillen@optimataxrelief.com")
driver.find_element(By.CSS_SELECTOR, "input[type='submit']").click()
driver.find_element(By.CSS_SELECTOR, "input[type='password']").send_keys("Opti%6&8$")
time.sleep(5)
driver.find_element(By.XPATH, "//input[@type='submit']").click()
#add twilio logic here
time.sleep(10)
driver.find_element(By.CSS_SELECTOR, "input[type='submit']").click()
time.sleep(5)
driver.find_element(By.CSS_SELECTOR, "input[type='submit']").click()
driver.find_element(By.CSS_SELECTOR, "button[id='O365_MainLink_NavMenu']").click()
driver.find_element(By.CSS_SELECTOR, "a[aria-label='Salesforce (Dev)']").click()
#driver.find_element(By.NAME, "name").send_keys("Brian Guillen")
#driver.find_element(By.NAME, "loginfmt").send_keys("Brian Guillen")


#driver.find_element(By.CSS_SELECTOR, "input[class='form-control ng-pristine ng-invalid ng-touched']").send_keys("Brian Guillen")


#driver.find_element(By.CSS_SELECTOR, "input[name = submit]").click()
#driver.find_element(By.CSS_SELECTOR, "input[name='loginfmt']").send_keys("bguillen@optimataxrelief.com")
#driver.find_element(By.CSS_SELECTOR, "input[name='email']").send_keys("bguillen@optimataxrelief.com")

#driver.find_element(By.NAME, "email").send_keys("Shetty")
#driver.find_element(By.ID, "exampleCheck1").click()
#driver.maximize_window()
#print(driver.title)
#print(driver.current_url)
#print(driver.find_element(By.CLASS_NAME, "alert-success").text)
#dropdown = Select(driver.find_element(By.ID, "exampleFormControlSelect1"))
#dropdown.select_by_visible_text("Female")
#dropdown.select_by_index(0)
#alert = driver.switch_to_alert
#print(alert.text)
#driver.close()
#driver.get("https://admin-dev.optimatax.com/")
#driver.minimize_window()
#driver.back()
#driver.refresh()
driver.switch_to_active_element()

