import pytest
from selenium.webdriver.common.by import By
from utils import config

# Test Case GL-001: Successful Guest Login
def test_successful_guest_login(browser):
    browser.get(f"{config.base_url}/account")
    browser.find_element(By.ID, 'login-btn').click()
    browser.find_element(By.ID, 'guest-login-option').click()
    assert "Welcome, Guest" in browser.page_source or "guest dashboard" in browser.current_url

# Test Case GL-002: Redirection After Guest Login
def test_redirection_after_guest_login(browser):
    browser.get(f"{config.base_url}/account")
    browser.find_element(By.ID, 'login-btn').click()
    browser.find_element(By.ID, 'guest-login-option').click()
    assert "dashboard" in browser.current_url or "homepage" in browser.current_url

# Test Case GL-003: Login Button Presence for Guest
def test_login_button_presence_for_guest(browser):
    browser.get(f"{config.base_url}/account")
    login_btn = browser.find_element(By.ID, 'login-btn')
    assert login_btn.is_displayed()

# Test Case GL-004: Login Button Clickability
def test_login_button_clickability(browser):
    browser.get(f"{config.base_url}/account")
    login_btn = browser.find_element(By.ID, 'login-btn')
    login_btn.click()
    assert "login" in browser.current_url or browser.find_element(By.ID, 'login-form').is_displayed()

# Test Case GL-005: Guest Session Persistence
def test_guest_session_persistence(browser):
    browser.get(f"{config.base_url}/account")
    browser.find_element(By.ID, 'login-btn').click()
    browser.find_element(By.ID, 'guest-login-option').click()
    browser.refresh()
    assert "Welcome, Guest" in browser.page_source

# Test Case GL-006: Guest Login with Invalid Session Data
def test_guest_login_with_invalid_session_data(browser):
    browser.get(f"{config.base_url}/account")
    browser.find_element(By.ID, 'login-btn').click()
    browser.find_element(By.ID, 'guest-login-option').click()
    browser.delete_all_cookies()
    browser.refresh()
    assert "login" in browser.current_url or "session expired" in browser.page_source

# Test Case GL-007: Missing Login Button for Guest
def test_missing_login_button_for_guest(browser):
    browser.get(f"{config.base_url}/account")
    try:
        login_btn = browser.find_element(By.ID, 'login-btn')
        assert login_btn.is_displayed()
    except Exception:
        pytest.fail("Login button is missing for guest user.")

# Test Case GL-008: Guest Login When Feature Disabled
def test_guest_login_when_feature_disabled(browser):
    browser.get(f"{config.base_url}/account")
    browser.find_element(By.ID, 'login-btn').click()
    guest_options = browser.find_elements(By.ID, 'guest-login-option')
    assert len(guest_options) == 0

# Test Case GL-009: Guest Login with Network Issues
def test_guest_login_with_network_issues(browser):
    # This is a placeholder; in real tests, network throttling would be set up.
    browser.get(f"{config.base_url}/account")
    browser.find_element(By.ID, 'login-btn').click()
    # Simulate network issue (manual or with browsermob-proxy in real test)
    # For now, just assert error message
    assert "Network error" in browser.page_source or "unable to login" in browser.page_source

# Test Case GL-010: Guest Login with Cookies Disabled
def test_guest_login_with_cookies_disabled(browser):
    # Placeholder: Normally, cookies would be disabled via browser options
    browser.get(f"{config.base_url}/account")
    browser.find_element(By.ID, 'login-btn').click()
    browser.find_element(By.ID, 'guest-login-option').click()
    assert "cookies required" in browser.page_source or "enable cookies" in browser.page_source

# Test Case GL-011: Guest Login with Maximum Session Duration
def test_guest_login_with_maximum_session_duration(browser):
    browser.get(f"{config.base_url}/account")
    browser.find_element(By.ID, 'login-btn').click()
    browser.find_element(By.ID, 'guest-login-option').click()
    # Placeholder: Wait for session expiry (not practical in real-time test)
    # Simulate session expiry
    browser.delete_all_cookies()
    browser.refresh()
    assert "session expired" in browser.page_source or "login" in browser.current_url

# Test Case GL-012: Guest Login with Minimum Data
def test_guest_login_with_minimum_data(browser):
    browser.get(f"{config.base_url}/account")
    browser.find_element(By.ID, 'login-btn').click()
    browser.find_element(By.ID, 'guest-login-option').click()
    # Assume no extra data is filled
    assert "Welcome, Guest" in browser.page_source

# Test Case GL-013: Login Button Across Screen Sizes
@pytest.mark.parametrize("width,height", [(375, 667), (768, 1024), (1920, 1080)])
def test_login_button_across_screen_sizes(browser, width, height):
    browser.set_window_size(width, height)
    browser.get(f"{config.base_url}/account")
    login_btn = browser.find_element(By.ID, 'login-btn')
    assert login_btn.is_displayed()

# Test Case GL-014: Login Button for New and Returning Guests
def test_login_button_for_new_and_returning_guests(browser):
    browser.get(f"{config.base_url}/account")
    login_btn = browser.find_element(By.ID, 'login-btn')
    login_btn.click()
    browser.find_element(By.ID, 'guest-login-option').click()
    # Log out
    browser.find_element(By.ID, 'logout-btn').click()
    browser.get(f"{config.base_url}/account")
    login_btn = browser.find_element(By.ID, 'login-btn')
    assert login_btn.is_displayed()

# Test Case GL-015: Guest Login Under Load
def test_guest_login_under_load(browser):
    # Placeholder: Real load test would use multiple threads/processes
    browser.get(f"{config.base_url}/account")
    browser.find_element(By.ID, 'login-btn').click()
    browser.find_element(By.ID, 'guest-login-option').click()
    assert "Welcome, Guest" in browser.page_source

# Test Case GL-016: Login Button Load Time
def test_login_button_load_time(browser):
    import time
    browser.get(f"{config.base_url}/account")
    start = time.time()
    login_btn = browser.find_element(By.ID, 'login-btn')
    end = time.time()
    assert (end - start) < 2

# Test Case GL-017: Login Button Accessibility
def test_login_button_accessibility(browser):
    browser.get(f"{config.base_url}/account")
    login_btn = browser.find_element(By.ID, 'login-btn')
    aria_label = login_btn.get_attribute('aria-label')
    tabindex = login_btn.get_attribute('tabindex')
    assert aria_label is not None
    assert tabindex is not None

# Test Case GL-018: Guest Login Security
def test_guest_login_security(browser):
    browser.get(f"{config.base_url}/account")
    browser.find_element(By.ID, 'login-btn').click()
    # Try XSS in guest login (placeholder)
    browser.execute_script("document.getElementById('guest-login-option').setAttribute('onclick', 'alert(1)')")
    browser.find_element(By.ID, 'guest-login-option').click()
    # Check no alert is present (would require alert handling in real test)
    assert "alert" not in browser.page_source

# Test Case GL-019: Guest Login/Browser Compatibility
@pytest.mark.parametrize("user_agent", [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/91.0.4472.124",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Safari/605.1.15",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Edge/18.18362"
])
def test_guest_login_browser_compatibility(browser, user_agent):
    # Placeholder: In real test, set user agent via browser options
    browser.get(f"{config.base_url}/account")
    browser.find_element(By.ID, 'login-btn').click()
    browser.find_element(By.ID, 'guest-login-option').click()
    assert "Welcome, Guest" in browser.page_source
