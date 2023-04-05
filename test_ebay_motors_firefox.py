from selenium import webdriver
import pytest
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_example_firefox(firefox):
    homepage_link = 'https://www.ebay.com/'
    firefox.maximize_window()
    # Navigate to SoundRise website
    firefox.get(homepage_link)

    firefox.find_element(By.LINK_TEXT, "Motors").click()
    assert 'Motors' in firefox.title
    assert 'Auto' in firefox.current_url


    def wait_for_dropdown_and_select_value(time, name, value):
        dropdown = WebDriverWait(firefox, timeout=time).until(EC.element_to_be_clickable((By.NAME, name)))
        Select(dropdown).select_by_visible_text(value)


    wait_for_dropdown_and_select_value(5, "Year", '2020')
    wait_for_dropdown_and_select_value(5, "Make", 'BMW')
    wait_for_dropdown_and_select_value(5, "Model", '220i')
    wait_for_dropdown_and_select_value(5, "Trim", 'Executive Coupe 2-Door')
    wait_for_dropdown_and_select_value(5, "Engine", '2.0L 1998CC 122Cu. In. l4 GAS DOHC Turbocharged')
    firefox.find_element(By.CLASS_NAME, 'motors-finder__find-btn').click()

    assert 'My Garage | eBay' in firefox.title
    assert '2020' in firefox.current_url
    assert 'BMW' in firefox.current_url
    assert '2-Door' in firefox.current_url
    assert '2.0L' in firefox.current_url
    assert '2520Turbocharged' in firefox.current_url

    firefox.quit()
