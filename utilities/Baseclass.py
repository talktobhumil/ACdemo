import pytest
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


@pytest.mark.usefixtures("setup")
class Baseclass:

    def verify_element_presence(self, locator):
      wait = WebDriverWait(self.driver, 10)
      wait.until(expected_conditions.presence_of_element_located(locator))

    def wait_for_element_clickable(self, locator):
        wait = WebDriverWait(self.driver, 10)
        wait.until(expected_conditions.element_to_be_clickable(locator))

