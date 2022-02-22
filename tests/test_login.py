import time
import pytest

from selenium import webdriver
from selenium.webdriver.common import alert
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

from PageObjects.LoginPage1 import LoginPage1
from PageObjects.RequestsPage import RequestPage
from PageObjects.VerifyPage import VerifyPage
from testdata.Loginpagedata import LoginPageData
from utilities.Baseclass import Baseclass


class TestLogin (Baseclass):

    def test_login(self):

        loginpage = LoginPage1(self.driver)
        loginpage.input_company_id()
        loginpage.input_phone_number()
        loginpage.send_code_action()

