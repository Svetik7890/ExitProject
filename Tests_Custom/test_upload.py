from Pages.page_custom_upload import PageCustom
import time
import os

def test_upload(chrome):
    page = PageCustom(chrome)
    page.openurl()
    page.trigger_popup_upload()
    time.sleep(2)
    page.chosefile()
    time.sleep(5)
    page.confirm_upload()
    time.sleep(2)
    # assert




