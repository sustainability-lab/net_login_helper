from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

from getpass import getpass

# Set options for headless mode
chrome_options = Options()
chrome_options.add_argument('--headless')  # Runs Chrome in headless mode.

# Create a webdriver instance with headless options
driver = webdriver.Chrome(options=chrome_options)
driver.implicitly_wait(5)
driver.set_page_load_timeout(5)
driver.set_script_timeout(5)

# URL to open
url = 'https://internet.iitgn.ac.in'

# Open the URL in the headless browser
driver.get(url)
WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.ID, "LoginUserPassword_auth_username")))
element = driver.find_element(By.ID, "LoginUserPassword_auth_username")
element.send_keys(input("Enter Username: "))
element = driver.find_element(By.ID, "LoginUserPassword_auth_password")
element.send_keys(getpass(prompt='Enter your password: '))
element = driver.find_element(By.ID, "UserCheck_Login_Button_span")
element.click()

# Wait a second!
WebDriverWait(driver, 1)

## Verify if internet is working
# get url till time-out
print("Login script executed")
print("Testing if internet is working...")
try:
    url = 'https://www.google.com'
    driver.get(url)
    # Checking if Google's search bar has been loaded.
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CLASS_NAME, "gLFyf")))
    print("Login Successfull")
except TimeoutException:
    print("Internet check failed")
