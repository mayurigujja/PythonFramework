from selenium.webdriver.common.by import By

from pageObjects.CheckOutPage import CheckOutPage


class HomePage:

    def __init__(self, driver):
        self.driver = driver

    shopLink = (By.LINK_TEXT, "Shop")

    def shopItems(self):
        #  self.driver.find_element_by_link_text("Shop").click()
        self.driver.find_element(*HomePage.shopLink).click()
        # Instead of creating checkout object in the teste2e(test case), we are creating it in the method that
        # clicks the shoplink, calls and returns the checkoutpage object
        checkoutpage = CheckOutPage(self.driver)
        return checkoutpage
