from selenium.webdriver.common.by import By
import os


class PageCustom:

    URLs = 'https://fineartamerica.com/custom'

    def __init__(self, driver):
        self.__driver=driver
        self.__uploadyourimage_button = (By.CLASS_NAME, 'ghostButton')
        self.__choosefile_button = (By.NAME, 'uploadimage')
        self.__upload_button = (By.ID, 'buttonInitiateUpload')


    def openurl(self):
        self.__driver.get(self.URLs)

    def trigger_popup_upload(self):
        element = self.__driver.find_element(*self.__uploadyourimage_button)
        element.click()

    def chosefile(self):
        element = self.__driver.find_element(*self.__choosefile_button)
        element.send_keys("C://Users//hp//PycharmProjects//pythonProject1//input_img.jpg")

    def confirm_upload(self):
        element = self.__driver.find_element(*self.__upload_button)
        element.click()