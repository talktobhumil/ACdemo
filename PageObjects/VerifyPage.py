import pytest
from selenium.webdriver.common.by import By

from PageObjects.Dashboard import Dashboard
from testdata.Loginpagedata import LoginPageData
from utilities.Baseclass import Baseclass


class VerifyPage(Baseclass):

    def __init__(self, driver):
        self.driver = driver

    verifyPhoneTitle = (By.CSS_SELECTOR, "span[class='MuiTypography-root mt-3 MuiTypography-h4']")
    firstOtpBox = (By.CSS_SELECTOR, "input[aria-label='Please enter verification code. Digit 1']")
    secondOtpBox = (By.CSS_SELECTOR, "input[aria-label='Digit 2']")
    thirdOtpBox = (By.CSS_SELECTOR, "input[aria-label='Digit 3']")
    fourthOtpBox = (By.CSS_SELECTOR, "input[aria-label='Digit 4']")

    def get_page_title(self):
        return self.driver.find_element(*VerifyPage.verifyPhoneTitle)

    def input_first_digit(self, get_data):
        self.driver.find_element(*VerifyPage.firstOtpBox).send_keys(get_data["otp"])

    def input_second_digit(self, get_data):
        self.driver.find_element(*VerifyPage.secondOtpBox).send_keys(get_data["otp"])

    def input_third_digit(self, get_data):
        self.driver.find_element(*VerifyPage.thirdOtpBox).send_keys(get_data["otp"])

    def input_fourth_digit(self, get_data):
        self.driver.find_element(*VerifyPage.fourthOtpBox).send_keys(get_data["otp"])


    @pytest.fixture(params=LoginPageData.test_login_page_data)
    def get_data(self, request):
        return request.param


