from selenium import webdriver
from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from pages import pages_data
from tests import test_data


class LoginPage(BasePage):
    def __init__(self, driver: webdriver.Chrome):
        super().__init__(driver)
        self.__userNameLocator = (By.XPATH, "//div[@id='ma']/span")
        self.__countOfAnnouncementsLocator = (By.XPATH, "//span[@class = 'c']")
        self.__settingsLocator = (By.ID, "idTabProfile")
        self.__contactInformationLocator = (By.XPATH, "//div[@id='tabmenu']//a")
        self.__phoneNumberLocator = (By.XPATH, "//div[@class='i phone']/div")
        self.__emailLocator = (By.XPATH, "//div[@class='i email']/div")

    def validate_user_name(self):
        userNameElement = self._find_element(self.__userNameLocator)
        assert userNameElement.text == pages_data.CUSTOMER_NAME

    def validate_count_of_my_announcements(self):
        countOfAnnouncementsElement = self._find_element(self.__countOfAnnouncementsLocator)
        assert int(countOfAnnouncementsElement.text) == 1

    def validate_contact_information(self):
        userNameElement = self._find_element(self.__userNameLocator)
        userNameElement.click()
        settingsElement = self._find_element(self.__settingsLocator)
        settingsElement.click()
        contactInformationElement = self._find_element(self.__contactInformationLocator)
        contactInformationElement.click()
        phoneNumberElement = self._find_element(self.__phoneNumberLocator)
        emailElement = self._find_element(self.__emailLocator)
        assert phoneNumberElement.text == pages_data.PHONE_NUMBER
        assert emailElement.text == test_data.VALID_USER_NAME
