from pages.base_page import BasePage
from selenium.webdriver.common.by import By 

class LoginPage(BasePage):
    LOGIN_LINK = (By.XPATH,"//a[normalize-space()='Log In']")
    USERNAME_INPUT = (By.XPATH, "//input[@id='customer_email']")
    PASSWORD_INPUT = (By.XPATH, "//input[@id='customer_password']")
    LOGIN_BUTTON = (By.XPATH, "//input[@value='Sign In']")
    SIGNUP_LINK = (By.XPATH,"//a[normalize-space() = 'Sign up']")
    SIGNUP_FIRST_NAME = (By.XPATH, "//input[@id='first_name']")
    SIGNUP_LAST_NAME = (By.XPATH, "//input[@id='last_name']")
    SIGNUP_EMAIL = (By.XPATH, "//input[@id='email']")
    SIGNUP_PASSWORD = (By.XPATH, "//input[@id='password']")
    SIGNUP_BUTTON = (By.XPATH, "//input[@value='Create']")
    LOG_OUT = (By.XPATH,"//a[normalize-space()='Log Out']")

    def __init__(self, driver):
        super().__init__(driver)

    def click_login_link(self):
        self.click_element(self.LOGIN_LINK)

    def enter_username(self,username):
        self.enter_text(self.USERNAME_INPUT, username)

    def enter_password(self,password):
        self.enter_text(self.PASSWORD_INPUT, password)

    def click_login(self):  
        self.click_element(self.LOGIN_BUTTON)

    def click_signup_link(self):
        self.click_element(self.SIGNUP_LINK)

    def enter_firstname_signup(self,first_name):
        self.enter_text(self.SIGNUP_FIRST_NAME, first_name)

    def enter_lastname_signup(self, last_name):
        self.enter_text(self.SIGNUP_LAST_NAME, last_name)

    def enter_email_signup(self, email):
        self.enter_text(self.SIGNUP_EMAIL, email)

    def enter_password_signup(self, signup_password):
        self.enter_text(self.SIGNUP_PASSWORD, signup_password)

    def click_signup_button(self):  
        self.click_element(self.SIGNUP_BUTTON)

        