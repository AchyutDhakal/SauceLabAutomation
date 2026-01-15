from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import allure
import os
import time

class BasePage():
    def __init__(self,driver):
        self.driver = driver
        self.wait = WebDriverWait(driver,10)

    def find_element(self,locator):
        return self.wait.until(EC.presence_of_element_located(locator))
    
    def find_clickable_element(self,locator):
        return self.wait.until(EC.element_to_be_clickable(locator))
    
    def find_visible_element(self,locator):
        return self.wait.until(EC.visibility_of_element_located(locator))
    
    def click_element(self,locator):
            try:
                element = self.find_clickable_element(locator)
                element.click()
            except Exception as e:
                element_name = locator.split('/'[-1]).replace('"', '').replace("'", "")
                self.take_screenshot(f"Click_failure_{element_name}")
                raise e

    def enter_text(self,locator, text):
            try:
                element = self.find_element(locator)
                element.clear()
                element.send_keys(text)
            except Exception as e:
                element_name = locator.split('/'[-1]).replace('"', '').replace("'", "")
                self.take_screenshot(f"Send_keys_failure_{element_name}")
                raise e

    def is_element_present(self, locator):
        try:
            self.find_element(locator)
            return True

        except TimeoutException:
            return False
        
    def is_element_visible(self,locator):
        try:
            self.find_visible_element(locator)
            return True
        
        except TimeoutException:
            return False

    def take_screenshot(self, name):
        screenshots_dir = "Screenshots"

        if not os.path.exists(screenshots_dir):
            os.makedirs(screenshots_dir)

        timestamp_str = int(time.time())
        file_name = f"{screenshots_dir}/{name}_{timestamp_str}.png"

        self.driver.save_screenshot(file_name)

        allure.attach.file(
            file_name,
            name=name,
            attachment_type = allure.attachment_type.PNG
        )

    def get_element_text(self, locator):
        element = self.find_element(locator)
        return element.text
        


