##############################################################################################################################################
# Selenium
# every browser invokes an executable file, this executable file is provided by the browser team
# selenium tests invokes this file which will execute the browser
# we can add a debug point on any line so that we can pause the execution to see what is happening
# whats the difference between relative and absolute path? - absolute is navigated from root html element downwards.  relative will try use an attribute instead
# relative is much better because any small change to the absolute path from the root will break the absolute path
##############################################################################################################################################

# About WebElement: A WebElement is a reference of any visible item (Button/TextField/CheckBox/Dropdown etc) in DOM (Document Object Model).
# Exception of a stale element reference is thrown in one of the two cases:
# If an element has been deleted.
# If an element is no longer attached to the DOM.
# “OpenQA.Selenium.StaleElementReferenceException” is thrown when reference of any element is first destroyed in DOM and then recreated by any Javascripts functions. This exception is commonly thrown in these scenarios. So, the reference of element becomes stale and we are no longer to use the reference to find the element in the DOM.
# The first possible solution to refresh the application instance using below code in Selenium:
# driver.navigate().refresh();
# By some of the ajax async calls in application, element is destroyed in DOM and recreated. We need to use below code to wait for the element to re-appear in the DOM.
# wait.until(ExpectedConditions.stalenessOf(webElement));
# If WebDriver throws a stale element exception in this case, even though the element still exists, the reference is lost. You should discard the current reference you hold and replace it, possibly by locating the element again once it is attached to the DOM.

##############################pytest#########################################################################################################
#  pip install python   /  pip install pytest-html
#  pytest --version
#  This is pytest version 5.4.1, imported from c:\python\lib\site-packages\pytest\__init__.py
#  test files should start with test_ or end with _test
#  pytest method names should start with test
#  test method names must be unique
#  method names are very important as they are basically the name of the test
#  @mark is the same as tags in cuke they are added like - @pytest.mark.smoke - py.test -m smoke
#  edit configurations can be added as "pytest" and then run with a target filename
#  any code should be wrapped in a method or it will not run, each method represents a new test case
#  you can also run the test from the command line, you must navigate to the package directory and then just run "py.test" command
#  "py.test -v" means verbose and will return further information (in the console)
#   @pytest.mark.skip - skip a specific test
#   @pytest.mark.xfail - remove a test from the test results
#   @pytest.fixture()
#    def setup():
#     print("Setup files")
#   def test_fixture_demo(setup):
#   a file named "conftest" can be used for each project to hold all the configuration - then all files will be able to access
#  "py.test -v -s" means verbose and will return further information (in the console), including the output of the methods
#   C:\Users\Matt\PycharmProjects\MasterPython\SeleniumCourse\pytestpackage>py.test test_set1.py -v - run a specific file by filename
#   C:\Users\Matt\PycharmProjects\MasterPython\SeleniumCourse\pytestpackage>py.test -k CreditCards - run a set of tests which match the regular expression
#   C:\Users\Matt\PycharmProjects\MasterPython\SeleniumCourse\pytestpackage>py.test --html=report.html
#   @pytest.mark.usefixtures("setup") - this can be used to run setup for all tests by adding them to a class instead
#   class TestExample:
#   @pytest.fixture(scope='class')  - adding a scope to the fixture like this means that it will only run once for the class instead of after each file
#   if a fixture has been declared globally, it still needs to be passed in if it is used in the test
#   datadriven tests can be done with return statements

##############################pytest#########################################################################################################

# waits
# choosing which wait to use depends on the strength of the application
# if one specific test requires a specific wait then dont want to apply for entire site
# long waits on all elements may allow bugs through
# depends on the environments being used also
from selenium import webdriver

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("headless")
chrome_options.add_argument("--ignore-certificate-errors")

driver = webdriver.Chrome(executable_path='C:\\seleniumdrivers\chromedriver.exe',options=chrome_options)

driver.get('https://the-internet.herokuapp.com/iframe')
print(driver.title)







