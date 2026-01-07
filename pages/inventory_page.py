from pages.base_page import BasePage


class InventoryPage(BasePage):
    """Inventory/Products page object model"""
    
    # Selectors
    INVENTORY_CONTAINER = ".inventory_container"
    PRODUCT_ITEM = ".inventory_item"
    PRODUCT_NAME = ".inventory_item_name"
    PRODUCT_PRICE = ".inventory_item_price"
    ADD_TO_CART_BUTTON = "button[data-test*='add-to-cart']"
    REMOVE_BUTTON = "button[data-test*='remove']"
    CART_BADGE = ".shopping_cart_badge"
    CART_LINK = ".shopping_cart_link"
    SORT_DROPDOWN = "[data-test='product_sort_container']"
    
    def is_inventory_page(self) -> bool:
        """Check if we're on inventory page"""
        return self.is_visible(self.INVENTORY_CONTAINER)
    
    def get_product_count(self) -> int:
        """Get number of products displayed"""
        return self.page.locator(self.PRODUCT_ITEM).count()
    
    def get_product_names(self) -> list:
        """Get all product names"""
        names = []
        for i in range(self.get_product_count()):
            name = self.page.locator(self.PRODUCT_NAME).nth(i).text_content()
            names.append(name)
        return names
    
    def get_product_prices(self) -> list:
        """Get all product prices"""
        prices = []
        for i in range(self.get_product_count()):
            price = self.page.locator(self.PRODUCT_PRICE).nth(i).text_content()
            prices.append(price)
        return prices
    
    def add_product_to_cart(self, product_index: int = 0):
        """Add product to cart by index"""
        self.page.locator(self.ADD_TO_CART_BUTTON).nth(product_index).click()
    
    def add_product_by_name(self, product_name: str):
        """Add product to cart by name"""
        product_locator = self.page.locator(
            f"//div[contains(text(), '{product_name}')]/ancestor::div[@class='inventory_item']//button[contains(@data-test, 'add-to-cart')]"
        )
        product_locator.click()
    
    def remove_product_from_cart(self, product_index: int = 0):
        """Remove product from cart by index"""
        self.page.locator(self.REMOVE_BUTTON).nth(product_index).click()
    
    def get_cart_badge_count(self) -> str:
        """Get cart badge count"""
        if self.is_visible(self.CART_BADGE):
            return self.get_text(self.CART_BADGE)
        return "0"
    
    def click_cart(self):
        """Click on cart link"""
        self.click(self.CART_LINK)
    
    def sort_products(self, sort_option: str):
        """Sort products by option"""
        # Use click and select instead of select_option for better compatibility
        dropdown = self.page.locator(self.SORT_DROPDOWN)
        dropdown.select_option(sort_option, timeout=5000)
