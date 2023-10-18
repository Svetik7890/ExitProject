import pytest
import logging
from selenium.webdriver.common.by import By
import time
import selenium


#no page object here yet, it my first try, PageObject present in login test
@pytest.mark.smoke
def test_global_search(chrome):
    chrome.get('https://fineartamerica.com/wall-art')
    global_search = chrome.find_element(By.ID, 'searchFormHeaderInput')
    global_search.send_keys('Sports Illustrated')
    search_button = chrome.find_element(By.ID, 'searchFormHeaderImageMagnifyingGlassLink')
    search_button.click()
    time.sleep(2)
    results_global_search = chrome.find_element(By.CLASS_NAME, 'searchEngineFeaturedProductLink')
    results_global_search.click()
    assert chrome.current_url == 'https://fineartamerica.com/shop/canvas+prints/sports+illustrated'

@pytest.mark.smoke
@pytest.mark.regression
def test_filter_search(chrome):
    chrome.get('https://fineartamerica.com/wall-art')
    abstract_check = chrome.find_element(By.PARTIAL_LINK_TEXT, 'Abstract')
    abstract_check.click()
    time.sleep(1)
    abstract_artists = chrome.find_element(By.ID, 'linkAvailableView_artist')
    abstract_artists.click()
    #I guess assertion is not required in each test, validation happens on the find element step









