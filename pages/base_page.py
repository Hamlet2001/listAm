from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver

    def _find_element(self, locator):
        if self._is_element_visible(locator):
            element = self.driver.find_element(*locator)
            return element
        else:
            exit(6)

    def _find_elements(self, locator):
        if self._is_elements_visible(locator):
            elements = self.driver.find_elements(*locator)
            return elements
        else:
            exit(6)

    def _is_element_visible(self, locator):
        try:
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))
            return True
        except:
            return False

    def _is_elements_visible(self, locator):
        try:
            WebDriverWait(self.driver, 10).until(EC.visibility_of_any_elements_located(locator))
            return True
        except:
            return False
