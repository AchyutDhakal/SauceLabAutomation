import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time

options = Options()
options.add_argument("--start-maximized")
options.page_load_strategy = "eager"

driver = webdriver.Chrome(options=options)

driver.get("https://sauce-demo.myshopify.com/")
time.sleep(5)

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


USERNAME = "achyutdhakal006@gmail.com"
PASSWORD = "Testtest7*"


wait = WebDriverWait(driver, 10)

def find_element(locator):
    return wait.until(EC.presence_of_element_located(locator))

def find_clickable_element(locator):
    return wait.until(EC.element_to_be_clickable(locator))

def enter_text(locator, text):
    element = find_element(locator)
    element.clear()
    element.send_keys(text)

def click_element(locator):
    element = find_clickable_element(locator)
    element.click()

def click_login_link():
    click_element(LOGIN_LINK)
    print("Clicked on login link")

def enter_username(username):
    enter_text(USERNAME_INPUT, username)
    print("Entered username")

def enter_password(password):
    enter_text(PASSWORD_INPUT, password)
    print("Entered password")

def click_login():  
    click_element(LOGIN_BUTTON)
    print("Clicked on login button")

def test_login(username, password):
    click_login_link()
    enter_username(username)
    enter_password(password)
    click_login()


def click_signup_link():
    click_element(SIGNUP_LINK)
    print("Clicked on signup link")
time.sleep(2)

def enter_firstname_signup():
    enter_text(SIGNUP_FIRST_NAME, "Achyut")
    print("Entered first name for signup")

def enter_lastname_signup():
    enter_text(SIGNUP_LAST_NAME, "Dhakal")
    print("Entered last name for signup")

def enter_email_signup():
    enter_text(SIGNUP_EMAIL, "achyutdhakal007@gmail.com")
    print("Entered email for signup")

def enter_password_signup():
    enter_text(SIGNUP_PASSWORD, "Testtest7*")
    print("Entered password for signup")

def click_signup():  
    click_element(SIGNUP_BUTTON)
    print("Clicked on signup button")

def test_signup():
    click_signup_link()
    if "register" in driver.current_url:
        print("User is on the signup page")
    else:
        print("User is not on the signup page")
    enter_firstname_signup()
    enter_lastname_signup()
    enter_email_signup()
    enter_password_signup()
    click_signup()

# def assert_true(condition, message):
#     assert condition, message

test_signup()
# assert_true("register" in driver.current_url, "User is not on the signup page")
test_login(USERNAME, PASSWORD)
if (EC.element_to_be_clickable(LOG_OUT)):
    print("Login successful, Log Out link is present.")
else:
    print("Login failed, Log Out link is not present.")

time.sleep(600)

driver.quit()
