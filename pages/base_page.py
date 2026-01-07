from playwright.sync_api import Page


class BasePage:
    """Base page class with common methods"""
    
    def __init__(self, page: Page):
        self.page = page
    
    def navigate(self, url: str):
        """Navigate to URL"""
        self.page.goto(url)
    
    def click(self, selector: str):
        """Click element"""
        self.page.click(selector)
    
    def fill(self, selector: str, text: str):
        """Fill input field"""
        self.page.fill(selector, text)
    
    def get_text(self, selector: str) -> str:
        """Get element text"""
        return self.page.text_content(selector)
    
    def is_visible(self, selector: str) -> bool:
        """Check if element is visible"""
        return self.page.is_visible(selector)
    
    def wait_for_element(self, selector: str, timeout: int = 5000):
        """Wait for element to appear"""
        self.page.wait_for_selector(selector, timeout=timeout)
    
    def get_title(self) -> str:
        """Get page title"""
        return self.page.title()
    
    def get_url(self) -> str:
        """Get current URL"""
        return self.page.url
