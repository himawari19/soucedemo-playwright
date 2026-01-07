from pages.base_page import BasePage


class LoginPage(BasePage):
    """Login page object model"""
    
    # Selectors
    USERNAME_INPUT = "[data-test='username']"
    PASSWORD_INPUT = "[data-test='password']"
    LOGIN_BUTTON = "[data-test='login-button']"
    ERROR_MESSAGE = "[data-test='error']"
    CONTAINER = ".login_container"
    
    def login(self, username: str, password: str):
        """Perform login"""
        self.fill(self.USERNAME_INPUT, username)
        self.fill(self.PASSWORD_INPUT, password)
        self.click(self.LOGIN_BUTTON)
    
    def get_error_message(self) -> str:
        """Get error message"""
        return self.get_text(self.ERROR_MESSAGE)
    
    def is_error_visible(self) -> bool:
        """Check if error message is visible"""
        return self.is_visible(self.ERROR_MESSAGE)
    
    def is_login_page(self) -> bool:
        """Check if we're on login page"""
        return self.is_visible(self.CONTAINER)
