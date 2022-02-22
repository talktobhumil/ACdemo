from selenium.webdriver.common.by import By

from PageObjects.RequestsPage import RequestPage


class Dashboard:

    def __init__(self, driver):
        self.driver = driver

    settingsIcon = (By.CSS_SELECTOR, "button[class='MuiButtonBase-root rounded-full']")
    notificationIcon = (By.CSS_SELECTOR, "span[class='MuiBadge-badge MuiBadge-anchorOriginTopRightRectangle MuiBadge-colorPrimary MuiBadge-invisible']")

    def assert_dashboard(self):
        return self.driver.find_element(*Dashboard.settingsIcon)

    def notification_icon(self):
        return self.driver.find_element(*Dashboard.notificationIcon)



