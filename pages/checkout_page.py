from pages.base_page import BasePage


class CheckoutPage(BasePage):
    """Checkout page object model"""
    
    # Selectors - Step One
    FIRST_NAME_INPUT = "[data-test='firstName']"
    LAST_NAME_INPUT = "[data-test='lastName']"
    POSTAL_CODE_INPUT = "[data-test='postalCode']"
    CONTINUE_BUTTON = "[data-test='continue']"
    ERROR_MESSAGE = "[data-test='error']"
    
    # Selectors - Step Two
    FINISH_BUTTON = "[data-test='finish']"
    TOTAL_PRICE = ".summary_total_label"
    
    # Selectors - Complete
    COMPLETE_HEADER = ".complete-header"
    COMPLETE_TEXT = ".complete-text"
    BACK_HOME_BUTTON = "[data-test='back-to-products']"
    
    def fill_checkout_info(self, first_name: str, last_name: str, postal_code: str):
        """Fill checkout information"""
        self.fill(self.FIRST_NAME_INPUT, first_name)
        self.fill(self.LAST_NAME_INPUT, last_name)
        self.fill(self.POSTAL_CODE_INPUT, postal_code)
    
    def continue_checkout(self):
        """Click continue button"""
        self.click(self.CONTINUE_BUTTON)
    
    def finish_checkout(self):
        """Click finish button"""
        self.click(self.FINISH_BUTTON)
    
    def get_error_message(self) -> str:
        """Get error message"""
        if self.is_visible(self.ERROR_MESSAGE):
            return self.get_text(self.ERROR_MESSAGE)
        return ""
    
    def is_error_visible(self) -> bool:
        """Check if error message is visible"""
        return self.is_visible(self.ERROR_MESSAGE)
    
    def get_total_price(self) -> str:
        """Get total price"""
        return self.get_text(self.TOTAL_PRICE)
    
    def is_order_complete(self) -> bool:
        """Check if order is complete"""
        return self.is_visible(self.COMPLETE_HEADER)
    
    def get_complete_message(self) -> str:
        """Get complete message"""
        return self.get_text(self.COMPLETE_TEXT)
    
    def back_to_home(self):
        """Click back to home button"""
        self.click(self.BACK_HOME_BUTTON)
