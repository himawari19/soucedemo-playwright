import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


class TestCheckout:
    """Test cases for checkout functionality"""
    
    @pytest.fixture(autouse=True)
    def setup_checkout(self, page, base_url):
        """Setup: Login, add products, and navigate to checkout"""
        login_page = LoginPage(page)
        login_page.navigate(base_url)
        login_page.login("standard_user", "secret_sauce")
        page.wait_for_url("**/inventory.html", timeout=5000)
        
        inventory_page = InventoryPage(page)
        inventory_page.add_product_to_cart(0)
        inventory_page.add_product_to_cart(1)
        inventory_page.click_cart()
        page.wait_for_url("**/cart.html", timeout=5000)
        
        cart_page = CartPage(page)
        cart_page.proceed_to_checkout()
        page.wait_for_url("**/checkout-step-one.html", timeout=5000)
    
    @pytest.mark.smoke
    @pytest.mark.checkout
    def test_checkout_step_one_displayed(self, page):
        """Test that checkout step one is displayed"""
        checkout_page = CheckoutPage(page)
        
        assert checkout_page.is_visible(checkout_page.FIRST_NAME_INPUT), "First name input should be visible"
        assert checkout_page.is_visible(checkout_page.LAST_NAME_INPUT), "Last name input should be visible"
        assert checkout_page.is_visible(checkout_page.POSTAL_CODE_INPUT), "Postal code input should be visible"
    
    @pytest.mark.smoke
    @pytest.mark.checkout
    def test_successful_checkout(self, page):
        """Test successful checkout flow"""
        checkout_page = CheckoutPage(page)
        
        checkout_page.fill_checkout_info("John", "Doe", "12345")
        checkout_page.continue_checkout()
        page.wait_for_url("**/checkout-step-two.html", timeout=5000)
        
        assert "checkout-step-two" in page.url, "Should navigate to checkout step two"
        
        checkout_page.finish_checkout()
        page.wait_for_url("**/checkout-complete.html", timeout=5000)
        
        assert checkout_page.is_order_complete(), "Order should be complete"
    
    @pytest.mark.regression
    @pytest.mark.checkout
    def test_checkout_with_empty_first_name(self, page):
        """Test checkout with empty first name"""
        checkout_page = CheckoutPage(page)
        
        checkout_page.fill_checkout_info("", "Doe", "12345")
        checkout_page.continue_checkout()
        
        assert checkout_page.is_error_visible(), "Error message should be visible"
        error_msg = checkout_page.get_error_message()
        assert "first name is required" in error_msg.lower(), "Should show first name required message"
    
    @pytest.mark.regression
    @pytest.mark.checkout
    def test_checkout_with_empty_last_name(self, page):
        """Test checkout with empty last name"""
        checkout_page = CheckoutPage(page)
        
        checkout_page.fill_checkout_info("John", "", "12345")
        checkout_page.continue_checkout()
        
        assert checkout_page.is_error_visible(), "Error message should be visible"
        error_msg = checkout_page.get_error_message()
        assert "last name is required" in error_msg.lower(), "Should show last name required message"
    
    @pytest.mark.regression
    @pytest.mark.checkout
    def test_checkout_with_empty_postal_code(self, page):
        """Test checkout with empty postal code"""
        checkout_page = CheckoutPage(page)
        
        checkout_page.fill_checkout_info("John", "Doe", "")
        checkout_page.continue_checkout()
        
        assert checkout_page.is_error_visible(), "Error message should be visible"
        error_msg = checkout_page.get_error_message()
        assert "postal code is required" in error_msg.lower(), "Should show postal code required message"
    
    @pytest.mark.regression
    @pytest.mark.checkout
    def test_checkout_step_two_displays_total(self, page):
        """Test that checkout step two displays total price"""
        checkout_page = CheckoutPage(page)
        
        checkout_page.fill_checkout_info("John", "Doe", "12345")
        checkout_page.continue_checkout()
        page.wait_for_url("**/checkout-step-two.html", timeout=5000)
        
        total_price = checkout_page.get_total_price()
        assert total_price, "Total price should be displayed"
        assert "$" in total_price, "Total price should contain $"
    
    @pytest.mark.regression
    @pytest.mark.checkout
    def test_complete_order_message(self, page):
        """Test complete order message"""
        checkout_page = CheckoutPage(page)
        
        checkout_page.fill_checkout_info("John", "Doe", "12345")
        checkout_page.continue_checkout()
        page.wait_for_url("**/checkout-step-two.html", timeout=5000)
        
        checkout_page.finish_checkout()
        page.wait_for_url("**/checkout-complete.html", timeout=5000)
        
        complete_msg = checkout_page.get_complete_message()
        assert complete_msg, "Complete message should be displayed"
        # Check for order dispatch message instead of thank you
        assert "dispatch" in complete_msg.lower() or "thank you" in complete_msg.lower(), "Should contain order confirmation message"
    
    @pytest.mark.regression
    @pytest.mark.checkout
    def test_back_to_home_from_complete(self, page):
        """Test back to home button from complete page"""
        checkout_page = CheckoutPage(page)
        
        checkout_page.fill_checkout_info("John", "Doe", "12345")
        checkout_page.continue_checkout()
        page.wait_for_url("**/checkout-step-two.html", timeout=5000)
        
        checkout_page.finish_checkout()
        page.wait_for_url("**/checkout-complete.html", timeout=5000)
        
        checkout_page.back_to_home()
        page.wait_for_url("**/inventory.html", timeout=5000)
        
        assert "inventory" in page.url, "Should navigate back to inventory page"
