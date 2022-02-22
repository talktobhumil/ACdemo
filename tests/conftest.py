import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )


@pytest.fixture(scope="class")
def setup(request):
    browser_name=request.config.getoption("browser_name")
    if browser_name == "chrome":
        driver = webdriver.Chrome(executable_path="D:\\Testing\\chromedriver.exe")
    elif browser_name == "firefox":
        driver = webdriver.Chrome(executable_path="D:\\Testing\\geckodriver.exe")
    elif browser_name == "IE":
        driver = webdriver.Chrome(executable_path="D:\\Testing\\IEdriver.exe")

    driver.get("https://a3atest.hectare.app/login")
    driver.implicitly_wait(20)
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()


