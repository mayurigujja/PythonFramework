from selenium.webdriver.common.by import By


class CheckOutPage:

    def __init__(self, driver):
        self.driver = driver

    # devices = self.driver.find_elements_by_css_selector("app-card-list.row app-card")
    devices = (By.CSS_SELECTOR, ".card-title a")
    phoneElement = (By.CSS_SELECTOR, ".card-footer button")
    phoneName = (By.CSS_SELECTOR, ".col-lg-3.col-md-6.mb-3 div div h4 a")
    clickphone = (By.XPATH, "div/div/button")
    checkoutbutton = (By.CSS_SELECTOR, "a[class*='btn-primary']")
    checkoutbutton2 = (By.CSS_SELECTOR, "button[class*='btn-success']")

    def getDevices(self):
        return self.driver.find_elements(*CheckOutPage.devices)

    def getPhoneElement(self):
        return self.driver.find_elements(*CheckOutPage.phoneElement)

    def getPhoneName(self):
        return self.driver.find_element(*CheckOutPage.phoneName)

    def ClickPhone(self):
        return self.driver.find_element(*CheckOutPage.clickphone)

    def getCheckoutButton(self):
        return self.driver.find_element(*CheckOutPage.checkoutbutton)

    def getCheckoutButton2(self):
        return self.driver.find_element(*CheckOutPage.checkoutbutton2)