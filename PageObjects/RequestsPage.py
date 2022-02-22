from selenium.webdriver.common.by import By


class RequestPage:

    def __init__(self, driver):
        self.driver = driver

    createCTA = (By.CSS_SELECTOR, "div[class='mt-3 sm:mt-0']")
    homeCleaningReq = (By.XPATH, "(//h2[@class='MuiTypography-root MuiTypography-subtitle1'])[2]")
    requestTab = (By.XPATH, "(//a[@role='button'])[3]")


    def access_create_cta(self):
        self.driver.find_element(*RequestPage.createCTA).click()

    def access_requesttab(self):
        self.driver.find_element(*RequestPage.requestTab).click()

    def select_homecleaning_type(self):
        self.driver.find_element(*RequestPage.homeCleaningReq).click()



