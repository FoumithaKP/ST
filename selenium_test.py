from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

options = Options()
options.add_experimental_option("detach", True)  # Keeps browser open after script
service = Service(executable_path="C:\\Users\\ASUS\\Downloads\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe")

driver = webdriver.Chrome(service=service, options=options)
driver.get("http://127.0.0.1:5000/")  # Make sure your Flask app is running!

# Interact with the form
driver.find_element(By.NAME, "num1").send_keys("10")
driver.find_element(By.NAME, "num2").send_keys("20")
driver.find_element(By.NAME, "operation").send_keys("subtraction")
driver.find_element(By.XPATH, "//input[@type='submit']").click()

# Wait and check result
time.sleep(2)
result = driver.find_element(By.TAG_NAME, "h2").text
print("Result from calculator:", result)
driver.quit()
