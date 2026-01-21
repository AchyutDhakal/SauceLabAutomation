import pytest
import time
import allure
from selenium.webdriver.chrome.options import Options
from pages.add_to_cart import AddToCart
from selenium import webdriver
from pages.search_page import SearchPage
from data.test_data import VALID_DATA
from utils.assertions import assert_true

class TestAddtocart():
    def setup_method(self):
        options = Options()
        options.add_argument("--start-maximized")
        options.add_argument("--headless=new")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")

        self.driver = webdriver.Chrome(options=options)
        self.driver.get("https://sauce-demo.myshopify.com/")

        self.add_to_cart = AddToCart(self.driver)
        self.search_page = SearchPage(self.driver)

    def teardown_method(self):
        self.driver.quit()

    @allure.title("Test Add To Cart feature")
    @pytest.mark.parametrize("data",VALID_DATA)
    def test_addtocart(self, data):
        with allure.step("Searching product"):
            self.search_page.search(data['search_keyword'])

        with allure.step("Assert searched product"):
            product_name = self.search_page.get_element_text(self.search_page.PRODUCT_NAME).lower()
            assert_true(data['search_keyword'].lower() in product_name,f"Actual and Expected do not match. Actual:{product_name} and Expected: {data['search_keyword'].lower()}", f"search_{data['search_keyword']}", self.search_page)

        with allure.step("Add product to the cart"):
            self.add_to_cart.click_add_to_cart_button()

        with allure.step("Assert add to cart"):
            time.sleep(3)
            self.add_to_cart.click_checkout_link()
            total_products = int(self.add_to_cart.find_element(self.add_to_cart.PRODUCTS_ON_CART).get_attribute("value"))
            assert_true(total_products>0,"No product is added to the cart","add_to_cart",self.add_to_cart)


        with allure.step("Checkout the product"):
            self.add_to_cart.click_checkout_button()

        with allure.step("Assert if the checkout is correct"):
            assert_true(self.add_to_cart.is_element_present(self.add_to_cart.PAYMENT_BUTTON),"Assertion failed as payment button is not present","checkout",self.add_to_cart)