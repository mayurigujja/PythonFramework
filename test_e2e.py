import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from Utilities.BaseClass import BaseClass
from conftest import setup
from pageObjects.CheckOutPage import CheckOutPage
from pageObjects.HomePage import HomePage


@pytest.mark.usefixtures()
# Inherit base class because base class has set up fixture that invokes the browser and opens the required URL
class TestOne(BaseClass):
    # self is necessary for the method if the method is declared inside a class
    def test_e2e(self):
        # set up fixture is passed with request parameter and the driver is assigned to the request
        # In order to access the driver of the other class, use self.driver
        # Call the homepage and assign an object
        homepage = HomePage(self.driver)
        # Access the shop items method that returns shop button element and click it
        homepage.shopItems().click()
        # Call the homepage and assign an object
        checkoutpage = CheckOutPage(self.driver)
        # Access the getDevices method to get the list of devices
        devices = checkoutpage.getDevices()
        for phone in devices:
            phoneElement = phone.find_element_by_css_selector(".col-lg-3.col-md-6.mb-3 div div h4 a")
            phoneName = phone.find_element_by_css_selector(".col-lg-3.col-md-6.mb-3 div div h4 a").text
            if phoneName == "Blackberry":
                phone.find_element_by_xpath("div/div/button").click()
        self.driver.find_element_by_css_selector("a[class*='btn-primary']").click()
        wait = WebDriverWait(self.driver, 10)
        wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, "button[class*='btn-success']")))
        self.driver.find_element_by_css_selector("button[class*='btn-success']").click()
        self.driver.find_element_by_id("country").send_keys("ind")
        wait.until(expected_conditions.presence_of_element_located((By.CLASS_NAME, "suggestions")))
        self.driver.find_element_by_xpath("//a[text()='India']").click()
        # driver.find_element_by_id("checkbox2").click()
        self.driver.find_element_by_css_selector("input[class*='btn-success']").click()
        successText = self.driver.find_element_by_css_selector("div[class*='alert-success']").text
        assert "Success! Thank you! Your order will be delivered in next few weeks" in successText
        # Screenshot is captured and stored in screen.png
        self.driver.get_screenshot_as_file("screen.png")
