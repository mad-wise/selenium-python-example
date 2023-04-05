from selenium import webdriver
import pytest
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.mytest
def test_ebay_motors():
    options = webdriver.ChromeOptions()
    serv = ChromeService(ChromeDriverManager().install())
    # Create browser variable and assign it to an instance of Chrome browser
    browser = webdriver.Chrome(service=serv, options=options)
    homepage_link = 'https://www.ebay.com/'
    browser.maximize_window()
    # Navigate to SoundRise website
    browser.get(homepage_link)

    browser.find_element(By.LINK_TEXT, "Motors").click()
    assert 'Motors' in browser.title
    assert 'Auto' in browser.current_url

    def wait_for_dropdown_and_select_value(time, name, value):
        dropdown = WebDriverWait(browser, timeout=time).until(EC.element_to_be_clickable((By.NAME, name)))
        Select(dropdown).select_by_visible_text(value)

    wait_for_dropdown_and_select_value(5, "Year", '2020')
    wait_for_dropdown_and_select_value(5, "Make", 'BMW')
    wait_for_dropdown_and_select_value(5, "Model", '220i')
    wait_for_dropdown_and_select_value(5, "Trim", 'Executive Coupe 2-Door')
    wait_for_dropdown_and_select_value(5, "Engine", '2.0L 1998CC 122Cu. In. l4 GAS DOHC Turbocharged')
    browser.find_element(By.CLASS_NAME, 'motors-finder__find-btn').click()

    assert 'My Garage | eBay' in browser.title
    assert '2020' in browser.current_url
    assert 'BMW' in browser.current_url
    assert '2-Door' in browser.current_url
    assert '2.0L' in browser.current_url
    assert '2520Turbocharged' in browser.current_url
