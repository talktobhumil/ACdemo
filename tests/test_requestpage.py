import time

import pytest

from PageObjects.LoginPage1 import LoginPage1
from PageObjects.RequestsPage import RequestPage
from PageObjects.VerifyPage import VerifyPage
from PageObjects.Dashboard import Dashboard
from PageObjects.HomecleaningRequest import HomeCleaningRequest
from testdata.Loginpagedata import LoginPageData
from utilities.Baseclass import Baseclass


class Testrequestpage (Baseclass):
    """"class contains methods for the request page"""

    def test_requestpage(self, get_data):
        LoginPage1.input_company_id(self, get_data)
        LoginPage1.input_phone_number(self, get_data)
        LoginPage1.send_code_action(self)
        VerifyPage.input_first_digit(self, get_data)
        VerifyPage.input_second_digit(self, get_data)
        VerifyPage.input_third_digit(self, get_data)
        VerifyPage.input_fourth_digit(self, get_data)
        self.verify_element_presence(Dashboard.settingsIcon)
        Dashboard.assert_dashboard(self)
        Dashboard.notification_icon(self)
        requestpage = RequestPage(self.driver)
        requestpage.access_requesttab()
        requestpage.access_create_cta()
        requestpage.select_homecleaning_type()
        currenturl = self.driver.current_url
        assert "requests" in currenturl
        hcr = HomeCleaningRequest(self.driver)
        print(hcr.get_form_title().text)
        hcr.select_unit()
        time.sleep(5)
        hcr.enter_request_details()



    @pytest.fixture(params=LoginPageData.test_login_page_data)
    def get_data(self, request):
        return request.param


