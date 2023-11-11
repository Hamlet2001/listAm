from tests import base_test
from tests import test_data

from pages.home_page.home_page import HomePage
from pages.login_page.login_page import LoginPage


class Tests(base_test.BaseTest):

    def test_language_selected_correct(self):
        self.homePageObject = HomePage(self.driver)
        self.homePageObject.select_the_language()
        self.homePageObject.validate_selected_language()

        self.homePageObject.validate_selected_language()

    def test_login_with_valid_credentials(self):
        self.homePageObject = HomePage(self.driver)
        self.homePageObject.select_the_language()
        self.homePageObject.click_on_my_account()
        self.homePageObject.fill_user_name_field(test_data.VALID_USER_NAME)
        self.homePageObject.fill_password_field(test_data.PASSWORD)
        self.homePageObject.click_to_sign_in_button()

        self.loginPageObject = LoginPage(self.driver)
        self.loginPageObject.validate_user_name()

    def test_check_contact_information(self):
        self.homePageObject = HomePage(self.driver)
        self.homePageObject.select_the_language()
        self.homePageObject.click_on_my_account()
        self.homePageObject.fill_user_name_field(test_data.VALID_USER_NAME)
        self.homePageObject.fill_password_field(test_data.PASSWORD)
        self.homePageObject.click_to_sign_in_button()

        self.loginPageObject = LoginPage(self.driver)
        self.loginPageObject.validate_contact_information()

    def test_number_of_my_announcements(self):
        self.homePageObject = HomePage(self.driver)
        self.homePageObject.select_the_language()
        self.homePageObject.click_on_my_account()
        self.homePageObject.fill_user_name_field(test_data.VALID_USER_NAME)
        self.homePageObject.fill_password_field(test_data.PASSWORD)
        self.homePageObject.click_to_sign_in_button()

        self.loginPageObject = LoginPage(self.driver)
        self.loginPageObject.validate_count_of_my_announcements()

    def test_search_result_city(self):
        self.homePageObject = HomePage(self.driver)
        self.homePageObject.select_the_language()
        self.homePageObject.search_text(test_data.SEARCHING_TEXT)

        self.homePageObject.validate_searching_results_cities()

    def test_login_with_invalid_credentials(self):
        self.homePageObject = HomePage(self.driver)
        self.homePageObject.select_the_language()
        self.homePageObject.click_on_my_account()
        self.homePageObject.fill_user_name_field(test_data.INVALID_USER_NAME)
        self.homePageObject.fill_password_field(test_data.PASSWORD)
        self.homePageObject.click_to_sign_in_button()

        self.homePageObject.validate_error_message()
