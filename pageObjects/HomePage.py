from selenium.webdriver.common.by import By

from pageObjects.CheckOutPage import CheckOutPage


class HomePage:

    def __init__(self, driver):
        self.driver = driver

    shopLink = (By.LINK_TEXT, "Shop")
    name = (By.NAME, "name")
    email = (By.NAME, "email")
    dropdown = (By.ID, "exampleFormControlSelect1")
    submit = (By.XPATH, "//input[@value='Submit']")

    def shopItems(self):
        #  self.driver.find_element_by_link_text("Shop").click()
        self.driver.find_element(*HomePage.shopLink).click()
        # Instead of creating checkout object in the teste2e(test case), we are creating it in the method that
        # clicks the shoplink, calls and returns the checkoutpage object
        checkoutpage = CheckOutPage(self.driver)
        return checkoutpage

    def getName(self):
        return self.driver.find_element(*HomePage.name)

    def getEmail(self):
        return self.driver.find_element(*HomePage.email)

    def getDropDown(self):
        return self.driver.find_element(*HomePage.dropdown)

    def getSubmit(self):
        return self.driver.find_element(*HomePage.submit)