from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time

options = Options()
options.add_argument("--start-maximized")

driver = webdriver.Chrome(options=options)

driver.get("https://accounts.saucelabs.com/am/XUI/#login/")
time.sleep(5)

USERNAME_INPUT = (By.ID, "//input[@id='idToken1']")
PASSWORD_INPUT = (By.ID, "//input[@id='idToken2']")
LOGIN_BUTTON = (By.ID, "//input[@id='loginButton_0']")
USERNAME = "oauth-achyutdhakal006-a430b"
PASSWORD = "8f23eb1e-3e4f-4e5c-99d4-d1dfd40bd40e"

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

def enter_username(username):
    enter_text(USERNAME_INPUT, username)

def enter_password(password):
    enter_text(PASSWORD_INPUT, password)

def click_login():  
    click_element(LOGIN_BUTTON)

def login(username, password):
    enter_username(username)
    enter_password(password)
    click_login()

login(USERNAME, PASSWORD)
