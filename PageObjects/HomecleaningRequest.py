import time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class HomeCleaningRequest:

    newRequesttitle = (By.CSS_SELECTOR, "h1[class='MuiTypography-root font-bold absolute left-12 -top-2 MuiTypography-subtitle1']")
    accessUnitDropDown = (By.XPATH, "(//div[@type='text'])[1]")
    enterUnit = (By.XPATH, "(//div[@class='jss134 css-2b097c-container'])[1]")
    eu = (By.ID, "model_id")
    select12Junit = (By.CSS_SELECTOR, "div[id='react-select-2-option-0']")
    requestDescription = (By.XPATH, "//*[@placeholder='Please tell us more about the issue']")

    def __init__(self, driver):
        self.driver = driver

    def get_form_title(self):
        return self.driver.find_element(*HomeCleaningRequest.newRequesttitle)

    def select_unit(self):
        self.driver.find_element(*HomeCleaningRequest.accessUnitDropDown).click()
        self.driver.find_element(*HomeCleaningRequest.eu).send_keys("12 J Unit A")
        time.sleep(3)
        self.driver.find_element(*HomeCleaningRequest.eu).send_keys(Keys.ENTER)

        time.sleep(3)


    def click_searched_unit(self):
        units = self.driver.find_elements(By.CSS_SELECTOR, "div[role='menuitem']" )

        for unit in units:
            if unit.text == "12 J Unit A":
                unit.click()
                print(unit.text)
                break

    def enter_request_details(self):
        self.driver.find_element(*HomeCleaningRequest.requestDescription).send_keys("TEST")


