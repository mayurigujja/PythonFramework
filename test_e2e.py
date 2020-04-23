import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from Utilities.BaseClass import BaseClass
from conftest import setup


@pytest.mark.usefixtures()
class TestOne(BaseClass):

    def test_e2e(self):

        self.driver.find_element_by_link_text("Shop").click()
        devices = self.driver.find_elements_by_css_selector("app-card-list.row app-card")
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
        self.driver.get_screenshot_as_file("screen.png")
