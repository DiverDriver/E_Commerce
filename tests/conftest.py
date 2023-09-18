import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.ie.service import Service
driver = None


def pytest_addoption(parser):
    parser.addoption("--browser_name", action="store", default="firefox")


@pytest.fixture(scope="class")
def setup(request):
    global driver
    browser_name = request.config.getoption("browser_name")
    if browser_name == "firefox":
        service_f = Service()
        driver = webdriver.Firefox(service=service_f)
    elif browser_name == "chrome":
        service_c = Service()
        driver = webdriver.Chrome(service=service_c)
    elif browser_name == "ie":
        service_ie = Service()
        driver = webdriver.Ie(service=service_ie)
    driver.get("https://rozetka.com.ua/")
    driver.maximize_window()
    driver.implicitly_wait(5)

    request.cls.driver = driver
