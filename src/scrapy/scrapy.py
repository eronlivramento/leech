from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By


class Scrapy:
    def __init__(self, url: str) -> None:
        self.url = url
        self.driver = self.__set_driver__()

    def start(self):
        """
        Start Driver and request to url
        """
        self.driver.get(self.url)

    def get_element_text(self, path: str) -> str:
        """
        Get Text on element path of the parameters

        :param path: str

        :return text to element
        """
        element = self.__get_element__(path)
        return element.text

    def check_if_exist(self, path: str) -> bool:
        """
        Check if exist element

        :param path: str

        :return bool element != None:
        """
        element = self.__get_element__(path)
        if element:
            return True

        return False

    def get_outer_html_element(self, path: str) -> str:
        """
        Get attribute 'outerHtml' on element of the path parameter
        :param path: str

        :return element.get_attribute("outerHTML")
        """
        element = self.__get_element__(path)
        return element.get_attribute("outerHTML")

    def click(self, path: str) -> bool:
        """
        Click on the element path of the parameters
        :param path: str
        """
        try:
            element = self.__get_element__(path)
            element.click()
            return True
        except Exception:
            pass

    def select_option(self, path: str, option: str) -> bool:
        """
        Select option in select tag

        :param path: str
        :param option: str
        """
        try:
            select = Select(self.__get_element__(path))
            select.select_by_value(option)
            return True
        except NoSuchElementException:
            pass

    def quit(self):
        """
        Close connection with webdriver
        """
        self.driver.quit()

    def __set_driver__(self):
        service = Service(ChromeDriverManager().install())
        options = webdriver.ChromeOptions()
        options.headless = True
        options.add_argument("--no-sandbox")
        return webdriver.Chrome(service=service, options=options)

    def __get_element__(self, path: str):
        try:
            return self.driver.find_element(By.XPATH, path)
        except NoSuchElementException:
            pass
