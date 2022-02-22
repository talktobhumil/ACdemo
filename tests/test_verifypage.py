import time

import pytest

from PageObjects.VerifyPage import VerifyPage
from testdata.Loginpagedata import LoginPageData
from utilities.Baseclass import Baseclass
from PageObjects.LoginPage1 import LoginPage1

class Testverifypage (Baseclass):
    """"class contains methods for the verification page"""

    def test_verifypage(self, get_data):
        LoginPage1.input_company_id(self, get_data)
        LoginPage1.input_phone_number(self, get_data)
        LoginPage1.send_code_action(self, get_data)
        verifypage = VerifyPage(self.driver)
        self.verify_element_presence(VerifyPage.verifyPhoneTitle)
        pagetitle = verifypage.get_page_title().text
        assert "Verify" in pagetitle
        print(pagetitle)
        verifypage.input_first_digit(get_data)
        verifypage.input_second_digit(get_data)
        verifypage.input_third_digit(get_data)
        verifypage.input_fourth_digit(get_data)

    @pytest.fixture(params=LoginPageData.test_login_page_data)
    def get_data(self, request):
        return request.param