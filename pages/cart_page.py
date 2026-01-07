from pages.base_page import BasePage


class CartPage(BasePage):
    """Shopping cart page object model"""
    
    # Selectors
    CART_CONTAINER = ".cart_list"
    CART_ITEM = ".cart_item"
    ITEM_NAME = ".inventory_item_name"
    ITEM_PRICE = ".inventory_item_price"
    ITEM_QUANTITY = ".cart_quantity"
    REMOVE_BUTTON = "button[data-test*='remove']"
    CONTINUE_SHOPPING = "[data-test='continue-shopping']"
    CHECKOUT_BUTTON = "[data-test='checkout']"
    EMPTY_MESSAGE = ".removed_cart_item"
    
    def is_cart_page(self) -> bool:
        """Check if we're on cart page"""
        return self.is_visible(self.CART_CONTAINER)
    
    def get_cart_items_count(self) -> int:
        """Get number of items in cart"""
        return self.page.locator(self.CART_ITEM).count()
    
    def get_cart_item_names(self) -> list:
        """Get all item names in cart"""
        names = []
        for i in range(self.get_cart_items_count()):
            name = self.page.locator(self.ITEM_NAME).nth(i).text_content()
            names.append(name)
        return names
    
    def get_cart_item_prices(self) -> list:
        """Get all item prices in cart"""
        prices = []
        for i in range(self.get_cart_items_count()):
            price = self.page.locator(self.ITEM_PRICE).nth(i).text_content()
            prices.append(price)
        return prices
    
    def remove_item_from_cart(self, item_index: int = 0):
        """Remove item from cart by index"""
        self.page.locator(self.REMOVE_BUTTON).nth(item_index).click()
    
    def continue_shopping(self):
        """Click continue shopping button"""
        self.click(self.CONTINUE_SHOPPING)
    
    def proceed_to_checkout(self):
        """Click checkout button"""
        self.click(self.CHECKOUT_BUTTON)
    
    def is_cart_empty(self) -> bool:
        """Check if cart is empty"""
        # Wait a moment for page to update
        self.page.wait_for_timeout(500)
        # Check if cart items are gone
        return self.page.locator(self.CART_ITEM).count() == 0
