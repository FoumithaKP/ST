import os
import time
import subprocess
from selenium import webdriver
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
    "sessionName": "Calculator UI Test",
    "local": "true",
    "seleniumVersion": "4.0.0",
    "userName": username,
    "accessKey": access_key
})

# Launch the remote browser
driver = webdriver.Remote(
    command_executor=f'https://{username}:{access_key}@hub-cloud.browserstack.com/wd/hub',
    options=chrome_options
)

# Run test
try:
    driver.get("http://127.0.0.1:5000/")
    time.sleep(2)
    assert "Calculator" in driver.title  # Assumes you set <title>Calculator</title> in your HTML
    print("Test Passed: Calculator title found.")
finally:
    driver.quit()
    print("Browser closed.")
    bs_process.terminate()
    print("BrowserStackLocal stopped.")
