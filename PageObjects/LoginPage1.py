import pytest
from selenium.webdriver.common.by import By

from PageObjects.VerifyPage import VerifyPage
from testdata.Loginpagedata import LoginPageData


class LoginPage1:
    companyId = (By.NAME, "companyId")
    phoneNumber = (By.NAME, "phone_number")
    sendCodeBtn = (By.XPATH, "//span[contains(text(),'SEND CODE')]")

    def __init__(self, driver):
        self.driver = driver

    '''To enter company id'''
    def input_company_id(self, get_data):
         self.driver.find_element(*LoginPage1.companyId).send_keys(get_data["companyid"])

    '''To enter phone number'''
    def input_phone_number(self, get_data):
         self.driver.find_element(*LoginPage1.phoneNumber).send_keys(get_data["phonenumber"])

    '''To click on send code button'''
    def send_code_action(self):
        self.driver.find_element(*LoginPage1.sendCodeBtn).click()

    '''testdata for login'''
    @pytest.fixture(params=LoginPageData.test_login_page_data)
    def get_data(self, request):
        return request.param





