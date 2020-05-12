import pytest
from selenium.webdriver.support.select import Select

from Utilities.BaseClass import BaseClass
from pageObjects.HomePage import HomePage


@pytest.mark.usefixtures()
class TestHomePage(BaseClass):
    def test_homepage(self, getData):
        homepage = HomePage(self.driver)
        homepage.getName().send_keys(getData["firstname"])
        homepage.getEmail().send_keys(getData["email"])
        select = Select(homepage.getDropDown())
        select.select_by_visible_text(getData["gender"])
        homepage.getSubmit().click()
        self.driver.refresh()




