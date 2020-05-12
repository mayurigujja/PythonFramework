import pytest
from selenium import webdriver


# Declare and initialize a run time variable - browser name
# Telling the pytest that you might expect the "browser_name" from the command line terminal
# If you don't give the below code and try to pass the "browser_name" in the cmd, it will not recognize it
from Tests.HomePageData import HomePageTestData


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )


# conftest contains all the fixtures that can be used to run as prerequisites to the test cases
@pytest.fixture(scope="class")
def setup(request):
    # to retrieve command line key value
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        # Invoking a browser is required before any test case
        driver = webdriver.Chrome(
            executable_path="C:\\Users\\mayurigu\\Downloads\\chromedriver_win32 (7)\\chromedriver.exe")
    elif browser_name == "firefox":
        driver = webdriver.Firefox(executable_path="C:\\Users\\mayurigu\\Downloads\\geckodriver.exe")
    driver.get("https://rahulshettyacademy.com/angularpractice")
    driver.maximize_window()
    # Assigning the local driver to the class driver so the driver can be usedx in the test cases
    request.cls.driver = driver
    yield
    driver.close()


@pytest.fixture(params=HomePageTestData.testdata)
def getData(request):
    return request.param
