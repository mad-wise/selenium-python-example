import time

from selenium import webdriver
import pytest
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

@pytest.mark.smoketest
def test_google_title():
    chrome_options = Options()
    chrome_options.add_argument("--lang=en")
    chrome_options.add_argument("--disable-extensions")
    browser = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
    browser.get("https://www.google.com")
    assert 'Google' == browser.title
    browser.find_element(By.NAME, "q").send_keys("Macbook Pro" + Keys.ENTER)
    assert 'Macbook Pro - Google Search' == browser.title
    time.sleep(3)
