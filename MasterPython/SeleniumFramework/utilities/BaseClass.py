import inspect
import logging

import pytest

#  this class is designed to hold all common utilities across the tests
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


@pytest.mark.usefixtures("setup")  # call the setup fixture one time before the tests runs to invoke the browser
class BaseClass:

    def verifylinktextpresent(self, text):
        WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located((By.LINK_TEXT, text)))

    def gotoaddress(self, url):
        self.driver.get(url)

    def checkpagetitlematchespassedtext(self, text):
        assert self.driver.title == text

    def selectdropdownoptionbytext(self, locator, text):
        sel = Select(locator)
        sel.select_by_visible_text(text)

    def getLogger(self):
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)  # this object is responsible for all logging - the name returns test name
        fileHandler = logging.FileHandler('logfile.log')  # say the file location and name
        formatter = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")
        fileHandler.setFormatter(formatter)

        logger.addHandler(fileHandler)  # must pass in a filehandler object (which is just the file location)

        logger.setLevel(
            logging.DEBUG)  # this level is in order DEBUG\INFO\WARN\ERROR\CRITICAL and will show only logs above set level

        return logger




