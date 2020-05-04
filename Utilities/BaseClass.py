import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


@pytest.mark.usefixtures("setup")
class BaseClass:

    def verifyPresence(self, selector, text):
        wait = WebDriverWait(self.driver, 10)
        wait.until(expected_conditions.presence_of_element_located((selector, text)))