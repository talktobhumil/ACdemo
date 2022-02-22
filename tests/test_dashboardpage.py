import pytest
import unittest

from PageObjects.Dashboard import Dashboard
from PageObjects.LoginPage1 import LoginPage1
from PageObjects.RequestsPage import RequestPage
from PageObjects.VerifyPage import VerifyPage
from testdata.Loginpagedata import LoginPageData
from utilities.Baseclass import Baseclass


class Testdashboardpage (Baseclass):
    """"class contains methods for the dashboard page"""

    def test_dashboardpage(self, get_data):
        LoginPage1.input_company_id(self, get_data)
        LoginPage1.input_phone_number(self, get_data)
        LoginPage1.send_code_action(self, get_data)
        VerifyPage.input_first_digit(self, get_data)
        VerifyPage.input_second_digit(self, get_data)
        VerifyPage.input_third_digit(self, get_data)
        VerifyPage.input_fourth_digit(self, get_data)
        dashboard = Dashboard(self.driver)
        if dashboard.assert_dashboard().size != 0:
            print("element exist!!")
        pageurl = self.driver.current_url
        assert "dashboard" in pageurl
        dashboard.notification_icon()


    @pytest.fixture(params=LoginPageData.test_login_page_data)
    def get_data(self, request):
        return request.param


