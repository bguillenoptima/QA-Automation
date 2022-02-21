from selenium import webdriver
import pytest
from selenium.webdriver.chrome.service import Service

from TestData.PagesData import PagesData


driver = None


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )
    parser.addoption(
        "--env_name", action="store", default="https://optimatax--develop.lightning.force.com/lightning/page/home"
    )


@pytest.fixture(scope="class", params=PagesData.pagesData)
def setup(request):
    global driver

    #browser_name = request.config.getoption("browser_name")
    browser_name = request.config.getoption("--browser_name")
    env_name = request.config.getoption("--env_name")

    if browser_name == "chrome":
        options = webdriver.ChromeOptions()
        options.add_argument("user-data-dir=C:\\Users\\OTRA155\\AppData\\Local\\Google\\Chrome\\User Data")
        options.add_argument("profile-directory=Profile 1")
        s = Service('C:\chromedriver.exe')
        driver = webdriver.Chrome(service=s, options=options)
        #driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe", chrome_options=options)
    elif browser_name == "firefox":
        driver = webdriver.Firefox(executable_path="C:\\geckodriver.exe")
    elif browser_name == "edge":
        driver = webdriver.Edge(executable_path="C:\\msedgedriver.exe")

    if env_name == "dev":
        driver.get("https://optimatax--develop.lightning.force.com/lightning/page/home")
    elif env_name == "staging":
        driver.get("https://optimatax--staging.lightning.force.com/lightning/page/home")
    elif env_name == "prod":
        driver.get("https://optimatax.lightning.force.com/lightning/page/home")

    driver.implicitly_wait(20)

    parameters = request.param
    request.cls.parameters = parameters
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

