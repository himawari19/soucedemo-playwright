import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage


class TestCart:
    """Test cases for shopping cart functionality"""
    
    @pytest.fixture(autouse=True)
    def login_and_add_products(self, page, base_url):
        """Login and add products before each test"""
        login_page = LoginPage(page)
        login_page.navigate(base_url)
        login_page.login("standard_user", "secret_sauce")
        page.wait_for_url("**/inventory.html", timeout=5000)
        
        inventory_page = InventoryPage(page)
        inventory_page.add_product_to_cart(0)
        inventory_page.add_product_to_cart(1)
        inventory_page.click_cart()
        page.wait_for_url("**/cart.html", timeout=5000)
    
    @pytest.mark.smoke
    @pytest.mark.cart
    def test_cart_page_displayed(self, page):
        """Test that cart page is displayed"""
        cart_page = CartPage(page)
        
        assert cart_page.is_cart_page(), "Should be on cart page"
    
    @pytest.mark.smoke
    @pytest.mark.cart
    def test_cart_items_displayed(self, page):
        """Test that cart items are displayed"""
        cart_page = CartPage(page)
        
        items_count = cart_page.get_cart_items_count()
        assert items_count == 2, "Should have 2 items in cart"
    
    @pytest.mark.regression
    @pytest.mark.cart
    def test_cart_item_names_displayed(self, page):
        """Test that cart item names are displayed"""
        cart_page = CartPage(page)
        
        item_names = cart_page.get_cart_item_names()
        assert len(item_names) == 2, "Should have 2 item names"
        assert all(name for name in item_names), "All item names should be non-empty"
    
    @pytest.mark.regression
    @pytest.mark.cart
    def test_cart_item_prices_displayed(self, page):
        """Test that cart item prices are displayed"""
        cart_page = CartPage(page)
        
        item_prices = cart_page.get_cart_item_prices()
        assert len(item_prices) == 2, "Should have 2 item prices"
        assert all(price for price in item_prices), "All item prices should be non-empty"
        assert all("$" in price for price in item_prices), "All prices should contain $"
    
    @pytest.mark.regression
    @pytest.mark.cart
    def test_remove_item_from_cart(self, page):
        """Test removing item from cart"""
        cart_page = CartPage(page)
        
        assert cart_page.get_cart_items_count() == 2, "Should have 2 items initially"
        
        cart_page.remove_item_from_cart(0)
        
        assert cart_page.get_cart_items_count() == 1, "Should have 1 item after removal"
    
    @pytest.mark.regression
    @pytest.mark.cart
    def test_remove_all_items_from_cart(self, page):
        """Test removing all items from cart"""
        cart_page = CartPage(page)
        
        cart_page.remove_item_from_cart(0)
        cart_page.remove_item_from_cart(0)
        
        assert cart_page.is_cart_empty(), "Cart should be empty"
    
    @pytest.mark.regression
    @pytest.mark.cart
    def test_continue_shopping(self, page):
        """Test continue shopping button"""
        cart_page = CartPage(page)
        
        cart_page.continue_shopping()
        
        page.wait_for_url("**/inventory.html", timeout=5000)
        assert "inventory" in page.url, "Should navigate back to inventory page"
    
    @pytest.mark.regression
    @pytest.mark.cart
    def test_proceed_to_checkout(self, page):
        """Test proceed to checkout button"""
        cart_page = CartPage(page)
        
        cart_page.proceed_to_checkout()
        
        page.wait_for_url("**/checkout-step-one.html", timeout=5000)
        assert "checkout-step-one" in page.url, "Should navigate to checkout page"
    
    @pytest.mark.regression
    @pytest.mark.cart
    def test_empty_cart_message(self, page):
        """Test empty cart message"""
        cart_page = CartPage(page)
        
        cart_page.remove_item_from_cart(0)
        cart_page.remove_item_from_cart(0)
        
        assert cart_page.is_cart_empty(), "Should show empty cart message"
