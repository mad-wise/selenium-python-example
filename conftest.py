import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService

@pytest.fixture()
def browser():
    options = webdriver.ChromeOptions()
    serv = ChromeService(ChromeDriverManager().install())
    # Create browser variable and assign it to an instance of Chrome browser
    browser = webdriver.Chrome(service=serv, options=options)
    yield browser
    browser.quit()

@pytest.fixture()
def firefox():
    options = webdriver.FirefoxOptions()
    serv = FirefoxService(GeckoDriverManager().install())
    # Create browser variable and assign it to an instance of Firefox browser
    firefox = webdriver.Chrome(service=serv, options=options)
    yield firefox
    firefox.quit()
