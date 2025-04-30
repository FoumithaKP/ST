import os
import time
import subprocess
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

# Your BrowserStack credentials
username = "foumithakp_R0TP48"
access_key = "MxSsbFj4ZtyfooBPzesM"

# Path to BrowserStackLocal binary
bs_local_path = "./BrowserStackLocal.exe"

# Start BrowserStackLocal
print("Starting BrowserStackLocal...")
bs_process = subprocess.Popen([bs_local_path, access_key])
time.sleep(5)  # Give it time to connect

# Define capabilities
chrome_options = Options()
chrome_options.set_capability("browserName", "Chrome")
chrome_options.set_capability("browserVersion", "latest")
chrome_options.set_capability("bstack:options", {
    "os": "Windows",
    "osVersion": "11",
    "sessionName": "Calculator Functional Test",
    "local": "true",
    "seleniumVersion": "4.0.0",
    "userName": username,
    "accessKey": access_key
})

# Launch browser
driver = webdriver.Remote(
    command_executor=f'https://{username}:{access_key}@hub-cloud.browserstack.com/wd/hub',
    options=chrome_options
)

# Run test
try:
    driver.get("http://127.0.0.1:5000/")
    time.sleep(2)

    # Fill the form
    driver.find_element(By.NAME, "num1").send_keys("10")
    driver.find_element(By.NAME, "num2").send_keys("5")
    operation_dropdown = driver.find_element(By.NAME, "operation")
    operation_dropdown.find_element(By.CSS_SELECTOR, "option[value='add']").click()

    # Submit the form
    driver.find_element(By.CSS_SELECTOR, "input[type='submit']").click()
    time.sleep(2)

    # Check for result
    result_text = driver.find_element(By.TAG_NAME, "h2").text
    assert "15" in result_text, f"Expected result 15, but got: {result_text}"
    print("Test Passed: Correct calculation result found.")

finally:
    driver.quit()
    print("Browser closed.")
    bs_process.terminate()
    print("BrowserStackLocal stopped.")
