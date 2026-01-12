from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pages.login_page import LoginPage
import allure
import time
import pytest
from data.test_data import VALID_DATA
from utils.assertions import assert_true

class TestSignup:
    def setup_method(self):
        options = Options()
        options.add_argument("--start-maximized")

        self.driver = webdriver.Chrome(options=options)
        self.driver.get("https://sauce-demo.myshopify.com/")

        self.login_page = LoginPage(self.driver)

    def teardown_method(self):
        self.driver.quit()

    @allure.title("Signup Testing")
    @pytest.mark.parametrize("valid_data", VALID_DATA )
    def test_signup(self, valid_data):
        with allure.step("Click signup link"):
            self.login_page.click_signup_link()
        
        with allure.step("Signup link click assertion"):
            assert_true("register" in self.driver.current_url, "User is not on the signup page")

        with allure.step("Fill out the signup form"):
            self.login_page.enter_firstname_signup(valid_data["first_name"])
            self.login_page.enter_lastname_signup(valid_data["last_name"])
            self.login_page.enter_email_signup(valid_data["email"])
            self.login_page.enter_password_signup(valid_data["signup_password"])

        with allure.step("Click signup button"):
            self.login_page.click_signup_button()

        with allure.step("Signup Assertion"):
            time.sleep(3)
            assert_true(self.login_page.is_element_visible(self.login_page.LOG_OUT), "Signup failed as logout is not present on the landing page.")

    @allure.title("Login Test with valid test data")
    @pytest.mark.parametrize("valid_data",VALID_DATA)
    def test_valid_login(self, valid_data):
        with allure.step("Click login link"):
            self.login_page.click_login_link()

        with allure.step("Login link click assertion"):
             assert_true("login" in self.driver.current_url, "User is not on the login page")
        
        with allure.step("Fill out login form and click login button"):
            self.login_page.enter_username(valid_data['username'])
            self.login_page.enter_password(valid_data['password'])
            self.login_page.click_login()

        with allure.step("Login Assertion"):
            time.sleep(3)
            assert_true(self.login_page.is_element_visible(self.login_page.LOG_OUT), "Login failed as logout button is not present")

