import pytest
from pages.login_page import LoginPage


class TestLogin:
    """Test cases for login functionality"""
    
    @pytest.mark.smoke
    @pytest.mark.login
    def test_successful_login(self, page, base_url):
        """Test successful login with valid credentials"""
        login_page = LoginPage(page)
        login_page.navigate(base_url)
        
        assert login_page.is_login_page(), "Should be on login page"
        
        login_page.login("standard_user", "secret_sauce")
        page.wait_for_url("**/inventory.html", timeout=5000)
        
        assert "inventory" in page.url, "Should redirect to inventory page"
    
    @pytest.mark.smoke
    @pytest.mark.login
    def test_login_with_locked_user(self, page, base_url):
        """Test login with locked user account"""
        login_page = LoginPage(page)
        login_page.navigate(base_url)
        
        login_page.login("locked_out_user", "secret_sauce")
        
        assert login_page.is_error_visible(), "Error message should be visible"
        error_msg = login_page.get_error_message()
        assert "locked out" in error_msg.lower(), "Should show locked out message"
    
    @pytest.mark.regression
    @pytest.mark.login
    def test_login_with_invalid_password(self, page, base_url):
        """Test login with invalid password"""
        login_page = LoginPage(page)
        login_page.navigate(base_url)
        
        login_page.login("standard_user", "wrong_password")
        
        assert login_page.is_error_visible(), "Error message should be visible"
        error_msg = login_page.get_error_message()
        assert "username and password do not match" in error_msg.lower(), "Should show invalid credentials message"
    
    @pytest.mark.regression
    @pytest.mark.login
    def test_login_with_invalid_username(self, page, base_url):
        """Test login with invalid username"""
        login_page = LoginPage(page)
        login_page.navigate(base_url)
        
        login_page.login("invalid_user", "secret_sauce")
        
        assert login_page.is_error_visible(), "Error message should be visible"
        error_msg = login_page.get_error_message()
        assert "username and password do not match" in error_msg.lower(), "Should show invalid credentials message"
    
    @pytest.mark.regression
    @pytest.mark.login
    def test_login_with_empty_username(self, page, base_url):
        """Test login with empty username"""
        login_page = LoginPage(page)
        login_page.navigate(base_url)
        
        login_page.login("", "secret_sauce")
        
        assert login_page.is_error_visible(), "Error message should be visible"
        error_msg = login_page.get_error_message()
        assert "username is required" in error_msg.lower(), "Should show username required message"
    
    @pytest.mark.regression
    @pytest.mark.login
    def test_login_with_empty_password(self, page, base_url):
        """Test login with empty password"""
        login_page = LoginPage(page)
        login_page.navigate(base_url)
        
        login_page.login("standard_user", "")
        
        assert login_page.is_error_visible(), "Error message should be visible"
        error_msg = login_page.get_error_message()
        assert "password is required" in error_msg.lower(), "Should show password required message"
    
    @pytest.mark.regression
    @pytest.mark.login
    def test_login_with_problem_user(self, page, base_url):
        """Test login with problem user"""
        login_page = LoginPage(page)
        login_page.navigate(base_url)
        
        login_page.login("problem_user", "secret_sauce")
        page.wait_for_url("**/inventory.html", timeout=5000)
        
        assert "inventory" in page.url, "Should redirect to inventory page"
    
    @pytest.mark.regression
    @pytest.mark.login
    def test_login_with_performance_glitch_user(self, page, base_url):
        """Test login with performance glitch user"""
        login_page = LoginPage(page)
        login_page.navigate(base_url)
        
        login_page.login("performance_glitch_user", "secret_sauce")
        page.wait_for_url("**/inventory.html", timeout=10000)
        
        assert "inventory" in page.url, "Should redirect to inventory page"
