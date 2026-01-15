from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class SearchPage(BasePage):
    SEARCH = (By.XPATH,"//input[@id='search-field']")
    PRODUCT = (By.XPATH,"(//img[@class='product'])[1]")
    PRODUCT_NAME = (By.XPATH,"//h1[@itemprop='name']")

    def __init__(self, driver):
        super().__init__(driver)

    def search(self, keyword):
        self.enter_text(self.SEARCH, keyword)
        self.click_element(self.PRODUCT)