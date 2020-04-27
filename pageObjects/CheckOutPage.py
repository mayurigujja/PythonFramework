from selenium.webdriver.common.by import By


class CheckOutPage:

    def __init__(self, driver):
        self.driver = driver

    # devices = self.driver.find_elements_by_css_selector("app-card-list.row app-card")
    devices = (By.CSS_SELECTOR, "app-card-list.row app-card")

    def getDevices(self):
        return self.driver.find_elements(*CheckOutPage.devices)