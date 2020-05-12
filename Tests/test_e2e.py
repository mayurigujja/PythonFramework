import pytest
from selenium.webdriver.common.by import By
from Utilities.BaseClass import BaseClass
from pageObjects.HomePage import HomePage


@pytest.mark.usefixtures()
# Inherit base class because base class has set up fixture that invokes the browser and opens the required URL
class TestOne(BaseClass):
    # self is necessary for the method if the method is declared inside a class
    def test_e2e(self):
        log = self.getLogger()
        print("HI")
        # set up fixture is passed with request parameter and the driver is assigned to the request
        # In order to access the driver of the other class, use self.driver
        # Call the homepage and assign an object
        homepage = HomePage(self.driver)
        # Access the shop items method that returns shop button element and click it
        checkoutpage = homepage.shopItems()
        # checkoutpage = CheckOutPage(self.driver)
        # -> Instead of creating checkout object here,
        # it is created in a method of home page that returns checkoutpage object
        # Access the getDevices method to get the list of devices
        devices = checkoutpage.getDevices()
        # devices = self.driver.find_elements_by_css_selector("app-card-list.row app-card")
        i = -1
        for phone in devices:
            i = i + 1
            phoneName = phone.text
            # phoneName = checkoutpage.getPhoneName().text
            if phoneName == "Blackberry":
               checkoutpage.getPhoneElement()[i].click()
        checkoutpage.getCheckoutButton().click()
        # VerifyPresence method is declared in the base class and used everywhere the wait is used
        self.verifyPresence(By.CSS_SELECTOR, "button[class*='btn-success']")
        self.driver.find_element_by_css_selector("button[class*='btn-success']").click()
        log.info("selecting india country")
        self.driver.find_element_by_id("country").send_keys("ind")
        self.verifyPresence(By.CLASS_NAME, "suggestions")
        self.driver.find_element_by_xpath("//a[text()='India']").click()
        # driver.find_element_by_id("checkbox2").click()
        self.driver.find_element_by_css_selector("input[class*='btn-success']").click()
        successText = self.driver.find_element_by_css_selector("div[class*='alert-success']").text
        assert "Success! Thank you! Your order will be delivered in next few weeks" in successText
        # Screenshot is captured and stored in screen.png
        self.driver.get_screenshot_as_file("screen.png")
