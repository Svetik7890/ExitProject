from selenium.webdriver.common.by import By



class PageDiscussions():

    URL = 'https://fineartamerica.com/discussions.html'

    def __init__(self,driver):
        self.__driver = driver
        self.__postanewtopic_button = (By.CLASS_NAME, 'button' )

    def openurl(self):
        self.__driver.get(self.URL)

    def postnewtopic(self):
        element = self.__driver.find_element(*self.__postanewtopic_button)
        element.click()