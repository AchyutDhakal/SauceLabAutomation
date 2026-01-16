from pages.base_page import BasePage
from selenium.webdriver.common.by import By
class AddToCart(BasePage):
    ADD_TO_CART_BUTTON = (By.XPATH,"//input[@id='add']")
    CART_ICON = (By.XPATH,"//a[@class='toggle-drawer cart desktop ']")
    CHECKOUT_LINK = (By.XPATH,"//a[@class='checkout']")
    CHECKOUT_BUTTON = (By.ID,"checkout")
    PAYMENT_BUTTON = (By.XPATH,"//button[@id='checkout-pay-button']")
    PRODUCTS_ON_CART = (By.XPATH,"//div[@class='one columns quantity tr']//input[@id='updates_611945025']")

    def __init__(self, driver):
        super().__init__(driver)

    def click_add_to_cart_button(self):
        self.click_element(self.ADD_TO_CART_BUTTON)

    def click_checkout_link(self):
        self.click_element(self.CHECKOUT_LINK)

    def click_checkout_button(self):
        self.click_element(self.CHECKOUT_BUTTON)