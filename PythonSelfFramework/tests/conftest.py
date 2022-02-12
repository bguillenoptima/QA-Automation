import time

from selenium import webdriver
import pytest
from TestData.PagesData import PagesData
from pageObjects.O365HomePage import O365HomePage
from pageObjects.O365LoginPages import O365LoginPages


driver = None

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
    request.cls.driver = driver
    yield
    driver.quit()

@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    """
        Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
        :param item:
        """
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = report.nodeid.replace("::", "_") + ".png"
            _capture_screenshot(file_name)
            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % file_name
                extra.append(pytest_html.extras.html(html))
        report.extra = extra


def _capture_screenshot(name):
        driver.get_screenshot_as_file(name)

@pytest.fixture(scope="class", params=PagesData.pagesData)
def dataLoad(request):
    return request.param

