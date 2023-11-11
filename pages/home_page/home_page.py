import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from pages import pages_data


class HomePage(BasePage):
    def __init__(self, driver: webdriver.Chrome):
        super().__init__(driver)
        self.__languagePopUpLocator = (By.ID, "dlgLangSel")
        self.__armLanguageLocator = (By.XPATH, f"//a[@href='/{pages_data.LANGUAGE}/']/img")
        self.__selectedLanguageLocator = (By.ID, "lbar")
        self.__myAccountFieldLocator = (By.ID, "ma")
        self.__userNameFieldLocator = (By.ID, "_idphone_number_or_email")
        self.__passwordFieldLocator = (By.ID, "_idpassword")
        self.__verificationLocator = (By.CLASS_NAME, "box2")
        self.__signInButtonLocator = (By.XPATH, "//input[@type='submit']")
        self.__errorMessageLocator = (By.XPATH, "//div[@class='error']/div/div/div")
        self.__searchInputLocator = (By.ID, "idSearchBox")
        self.__resultsItemsLocator = (By.XPATH, "//div[@class='dl']//div[@class='at']")

    def select_the_language(self):
        armLanguageElement = self._find_element(self.__armLanguageLocator)
        armLanguageElement.click()

    def validate_selected_language(self):
        selectedLanguageElement = self._find_element(self.__selectedLanguageLocator)
        assert selectedLanguageElement.get_attribute("class") == pages_data.LANGUAGE

    def click_on_my_account(self):
        myAccountElement = self._find_element(self.__myAccountFieldLocator)
        myAccountElement.click()

    def fill_user_name_field(self, user_name):
        userNameFieldElement = self._find_element(self.__userNameFieldLocator)
        userNameFieldElement.clear()
        userNameFieldElement.send_keys(user_name)

    def fill_password_field(self, passwd):
        passwordFieldElement = self._find_element(self.__passwordFieldLocator)
        passwordFieldElement.clear()
        passwordFieldElement.send_keys(passwd)

    def click_to_sign_in_button(self):
        try:
            if self._find_element(self.__verificationLocator).is_displayed():
                time.sleep(10)
        except:
            pass
        signInButtonElement = self._find_element(self.__signInButtonLocator)
        signInButtonElement.click()

    def validate_error_message(self):
        errorMessageElement = self._find_element(self.__errorMessageLocator)
        assert errorMessageElement.text == pages_data.ERROR_MESSAGE

    def search_text(self, text):
        searchInputElement = self._find_element(self.__searchInputLocator)
        searchInputElement.clear()
        searchInputElement.send_keys(text)
        searchInputElement.send_keys(Keys.ENTER)

    def validate_searching_results_cities(self):
        resultsItemsElements = self._find_elements(self.__resultsItemsLocator)
        listOfResultsCities = []
        for el in resultsItemsElements:
            listOfResultsCities.append(el.text)
        for index in range(len(listOfResultsCities)):
            assert listOfResultsCities[index].split(",")[0] == pages_data.CITY
