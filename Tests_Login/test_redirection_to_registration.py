from Pages.page_discussions import PageDiscussions
from selenium.webdriver.common.by import By
import time




#Assertion absent as page is not implemented yet or incorrect redirection
def test_here_registration_link(chrome):
    page = PageDiscussions(chrome)
    page.openurl()
    page.postnewtopic()
    #url_posttopic_page = chrome.current_url
    here_textlink = chrome.find_element(By.CSS_SELECTOR, "a[href='/openanaccountdiscussions.html']")
    here_textlink.click()
    time.sleep(2) #page not found
