import unittest
from selenium import webdriver

from tests import test_data


class BaseTest(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)
        self.driver.delete_all_cookies()
        self.driver.maximize_window()
        self.driver.get(test_data.HOME_URL)

    def tearDown(self) -> None:
        self.driver.close()
