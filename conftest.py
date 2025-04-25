import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from configtestdata import *
from selenium.webdriver.common.alert import Alert

@pytest.fixture(scope="class", autouse=True)
def setup(request):
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    driver.get(BaseUrl)

    request.cls.driver = driver
    yield driver
    driver.quit()
    alert = Alert(driver)
    alert.accept()
