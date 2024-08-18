from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# The webdriver management will be handled by the browserstack-sdk
# so tests will run browserstack without any changes to the test files!

options = ChromeOptions()
options.set_capability('sessionName', 'Amazon Login Test')

driver = webdriver.Remote(
    command_executor='http://localhost:4444/wd/hub',
    options=options)

driver.maximize_window()
driver.implicitly_wait(3)

try:

    # Navigate to Amazon sign-in page
    driver.get("https://www.amazon.in/")

    # Click the "Account & Lists" button
    account_button = driver.find_element(By.ID, "nav-link-accountList-nav-line-1")
    account_button.click()

    # Wait until the username page loads
    wait = WebDriverWait(driver, 10)
    continue_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@type= 'submit']")))

    # Fill in the username/email id
    email_field = driver.find_element(By.XPATH, "//input[@name= 'email']")
    email_field.send_keys("9655893313")
    email_field.send_keys(Keys.RETURN)

    # Wait until the password page loads
    wait = WebDriverWait(driver, 10)
    login_button = wait.until(EC.element_to_be_clickable((By.ID, 'signInSubmit')))

    # Fill in the password
    password_field = driver.find_element(By.XPATH, "//input[@name= 'password']")
    password_field.send_keys("123456")
    password_field.send_keys(Keys.RETURN)

    # Wait until the home page loads
    actual_welcome_message = driver.find_element(By.XPATH, "//*[@id='nav-link-accountList-nav-line-1']").text
    print(actual_welcome_message)

    # Fetch the welcome message in the home page and validate
    expected_welcome_message = "Hello, Vinitha"
    assert expected_welcome_message == actual_welcome_message
    print("Login validation passed")

except Exception as e:
    print("Login validation failed " + str(e))

finally:
    # Close the browser
    driver.quit()
