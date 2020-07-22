import time

import pytest

from SeleniumFramework.pages.Home import HomePage
from SeleniumFramework.testdata.HomePageData import HomePageData
from SeleniumFramework.utilities.BaseClass import BaseClass


class TestHomePage(BaseClass):



    def test_form_submission(self, getdata):
        log = self.getLogger()
        home_page = HomePage(self.driver)
        # home_page.e_name_field().send_keys(getdata[0]) # you can get the value by index values when passing tuple for each dataset
        home_page.e_name_field().send_keys(getdata["Firstname"])
        home_page.e_email_field().send_keys(getdata["Surname"])
        home_page.e_password_field().send_keys("mattspassword")
        home_page.e_checkbox().click()
        self.selectdropdownoptionbytext(home_page.e_gender(), getdata["Gender"])
        home_page.e_employment_radio_employed().click()
        home_page.e_dob().send_keys("16041807")
        home_page.e_submit().click()
        assert "Success" in home_page.e_success_message().text
        self.driver.refresh()  # clear the page for the next data run
        #time.sleep(5)
        log.info("Firstname" + " : " + getdata["Firstname"])
        log.info("Surname" + " : " + getdata["Surname"])
        log.info("Gender" + " : " + getdata["Gender"])

    #@pytest.fixture(params=HomePageData.getTestData("Testcase2"))
    @pytest.fixture(params=HomePageData.test_home_page_data)
    def getdata(self, request):
        return request.param
