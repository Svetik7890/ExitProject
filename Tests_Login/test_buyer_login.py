from Pages.page_login_buyer import PageBuyerLogin
import time


def test_login_buyer(chrome):
    page = PageBuyerLogin(chrome)
    page.openurl()
    page.setusername('sv.refahi@gmail.com')
    page.setpassword('XNRMXCXA')
    page.login()
    time.sleep(5)
    assert chrome.current_url == 'https://fineartamerica.com/collectors/collectorprofile.php'




