from selenium.webdriver.support.select import Select

from Utilities.BaseClass import BaseClass


class HomePage(BaseClass):
    def test_form(self):
        self.driver.find_element_by_name("name").send_keys("Mayuri")
        self.driver_find_element_by_name("email").send_keys("gujja.mayuri@gmail.com")
        select = Select(self.driver_find_element_by_id("exampleFormControlSelect1"))
        select.select_by_visible_text("Male")
        self.driver.find_element_by_xpath("//input[@value='Submit']").click()


