from selenium.webdriver.common.by import By


class PageBuyerLogin:

    URLs = 'https://fineartamerica.com/logincollector.php'

    def __init__(self, driver):
        self.__driver=driver
        self.__username_field = (By.ID, 'username')
        self.__password_field = (By.ID, 'password')
        self.__login_button = (By.CLASS_NAME, 'button')


    def openurl(self):
        self.__driver.get(self.URLs)

    def setusername(self, username: str) -> None:
        element = self.__driver.find_element(*self.__username_field)
        element.clear()
        element.send_keys(username)

    def setpassword(self, password: str) -> None:
        element = self.__driver.find_element(*self.__password_field)
        element.clear()
        element.send_keys(password)

    def login(self) -> None:
        element = self.__driver.find_element(*self.__login_button)
        element.click()