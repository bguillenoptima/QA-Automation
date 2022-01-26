import time

from selenium import webdriver
import pytest

from pageObjects.O365EmailPage import O365EmailPage
from pageObjects.O365HomePage import O365HomePage


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )


@pytest.fixture(scope="class")
def setup(request):
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
    elif browser_name == "firefox":
        driver = webdriver.Firefox(executable_path="C:\\geckodriver.exe")
    elif browser_name == "edge":
        driver = webdriver.Edge(executable_path="C:\\msedgedriver.exe")
    driver.implicitly_wait(20)
    driver.get("https://portal.office365.com")
    driver.maximize_window()
    office_email_page = O365EmailPage(driver)
    office_email_page.email_items()
    office_pw_page = office_email_page.email_next_button()
    time.sleep(1)
    office_pw_page.send_password()
    office_multi_factor_auth = office_pw_page.password_next()
    # add twilio logic here
    time.sleep(10)
    office_multi_factor_auth.click_verify()
    time.sleep(2)
    office_multi_factor_auth.click_verify()
    office_homepage = O365HomePage(driver)
    office_homepage.click_waffle()
    office_homepage.click_sf_dev()
    request.cls.driver = driver

