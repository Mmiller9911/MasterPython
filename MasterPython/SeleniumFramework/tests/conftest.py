import pytest
from selenium import webdriver
driver = None  # because of this global driver all the steps below will use the same object
# this is only for when things can be used across multiple cases


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"  # store the browser_name as passed via command line using chrome if argument is not passed through
    )


@pytest.fixture(scope="class")  # do this once for the entire class
def setup(request):
    global driver
    browser_name = request.config.getoption("browser_name")
    if browser_name == 'chrome':  # py.test --browser_name chrome
        driver = webdriver.Chrome(executable_path='C:\\seleniumdrivers\chromedriver.exe')

    elif browser_name == 'firefox':  # py.test --browser_name firefox
        driver = webdriver.Firefox(executable_path='C:\\seleniumdrivers\geckodriver.exe')

    elif browser_name == 'ie':  # py.test --browser_name ie
        driver = webdriver.Ie(executable_path='C:\\seleniumdrivers\IEDriverServer.exe')

    driver.get('https://rahulshettyacademy.com/angularpractice/')
    driver.maximize_window()

    request.cls.driver = driver  # assign this local driver to the calling class driver - using request this is auto passed through
    yield
    driver.close()


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
