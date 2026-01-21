import pytest
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from pages.search_page import SearchPage
import allure
from data.test_data import VALID_DATA
from utils.assertions import assert_true, assert_equal
import time

class TestSearch():
    def setup_method(self):
        options = Options()
        options.add_argument("--start-maximized")
        options.add_argument("--headless=new")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")

        self.driver = webdriver.Chrome(options=options)
        self.driver.get("https://sauce-demo.myshopify.com/")

        self.search_page = SearchPage(self.driver)

    def teardown_method(self):
        self.driver.quit()

    @allure.title("Testing Search")
    @pytest.mark.parametrize("data",VALID_DATA)
    def test_search(self, data):
        with allure.step(f"Search {data['search_keyword']}"):
            self.search_page.search(data['search_keyword'])

        product_name = self.search_page.get_element_text(self.search_page.PRODUCT_NAME).lower()
        time.sleep(2)
        
        with allure.step("Assert searched product"):
            assert_true(data['search_keyword'].lower() in product_name,f"Actual and Expected do not match. Actual:{product_name} and Expected: {data['search_keyword'].lower()}", f"search_{data['search_keyword']}", self.search_page)
    