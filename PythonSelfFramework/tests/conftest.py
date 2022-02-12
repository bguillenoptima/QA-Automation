import time

from selenium import webdriver
import pytest
import logging
from TestData.PagesData import PagesData
from pageObjects.O365HomePage import O365HomePage
from pageObjects.O365LoginPages import O365LoginPages


driver = None

logger = logging.getLogger(__name__)

fileHandler = logging.FileHandler('logfile.log')

logger.addHandler(fileHandler)  #filehandler object
logger.debug("A debug statement is executed")
logger.info("Information statement")
logger.debug("A debug statement is executed")

def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )


@pytest.fixture(scope="class")
def setup(request):
    global driver
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
    elif browser_name == "firefox":
        driver = webdriver.Firefox(executable_path="C:\\geckodriver.exe")
    elif browser_name == "edge":
        driver = webdriver.Edge(executable_path="C:\\msedgedriver.exe")

    driver.maximize_window()
    driver.implicitly_wait(20)
    driver.get("https://portal.office365.com")
    officeLoginPages = O365LoginPages(driver)

    officeLoginPages.email_field().send_keys(PagesData.pagesData[0]["tester_email"])
    officeLoginPages.next_button().click()

    time.sleep(1)

    officeLoginPages.password_field().send_keys(PagesData.pagesData[0]["tester_password"])
    officeLoginPages.next_button().click()

    # add twilio logic here
    time.sleep(10)

    officeLoginPages.next_button().click()

    time.sleep(2)

    officeLoginPages.next_button().click()

    office_homepage = O365HomePage(driver)
    office_homepage.waffle_icon().click()
    office_homepage.sf_dev_button().click()
    tabs = driver.window_handles
    logger.debug(tabs)
    request.cls.driver = driver
    yield
    driver.quit()

@pytest.fixture(scope="class", params=PagesData.pagesData)
def dataLoad(request):
    return request.param

