from selenium.webdriver.common.by import By


class HomePage:

    def __init__(self, driver):
        self.driver = driver

    shopLink = (By.LINK_TEXT, "Shop")

    def shopItems(self):
        #  self.driver.find_element_by_link_text("Shop").click()
        return self.driver.find_element(*HomePage.shopLink)