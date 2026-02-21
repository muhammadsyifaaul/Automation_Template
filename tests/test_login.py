import os
import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture(scope="module")
def driver():
    # Set up Chrome options for headless mode if required by CI/CD
    chrome_options = Options()
    if os.environ.get('CI') == 'true' or os.environ.get('GITHUB_ACTIONS') == 'true':
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')

    # Initialize WebDriver
    service = Service(ChromeDriverManager().install())
    driver_instance = webdriver.Chrome(service=service, options=chrome_options)
    
    # Get the absolute path to the local HTML file
    current_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    file_path = f"file:///{os.path.join(current_dir, 'webapp', 'index.html').replace(chr(92), '/')}"
    
    # Store path for tests to use
    driver_instance.file_path = file_path
    
    yield driver_instance
    
    # Teardown
    driver_instance.quit()

def test_login_success(driver):
    driver.get(driver.file_path)
    time.sleep(0.5)
    
    username_input = driver.find_element(By.ID, 'username')
    password_input = driver.find_element(By.ID, 'password')
    login_btn = driver.find_element(By.ID, 'loginBtn')
    
    username_input.send_keys('admin')
    password_input.send_keys('password123')
    login_btn.click()
    
    time.sleep(0.5)
    message_element = driver.find_element(By.ID, 'loginMessage')
    assert "Login successful!" in message_element.text
    assert "success" in message_element.get_attribute('class')

def test_login_invalid_credentials(driver):
    driver.get(driver.file_path)
    time.sleep(0.5)
    
    username_input = driver.find_element(By.ID, 'username')
    password_input = driver.find_element(By.ID, 'password')
    login_btn = driver.find_element(By.ID, 'loginBtn')
    
    username_input.send_keys('wronguser')
    password_input.send_keys('wrongpass')
    login_btn.click()
    
    time.sleep(0.5)
    message_element = driver.find_element(By.ID, 'loginMessage')
    assert "Invalid username or password" in message_element.text
    assert "error" in message_element.get_attribute('class')

def test_login_empty_fields(driver):
    driver.get(driver.file_path)
    time.sleep(0.5)
    
    login_btn = driver.find_element(By.ID, 'loginBtn')
    login_btn.click()
    
    time.sleep(0.5)
    username_error = driver.find_element(By.ID, 'usernameError')
    password_error = driver.find_element(By.ID, 'passwordError')
    
    assert "Username is required" in username_error.text
    assert "Password is required" in password_error.text
