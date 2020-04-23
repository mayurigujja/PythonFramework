import pytest
from selenium import webdriver


@pytest.fixture(scope="class")
def setup(request):

    driver = webdriver.Chrome(executable_path="C:\\Users\\mayurigu\\Downloads\\chromedriver_win32 (7)\\chromedriver.exe")
    driver.get("https://rahulshettyacademy.com/angularpractice")
    driver.maximize_window()
    request.cls.driver = driver