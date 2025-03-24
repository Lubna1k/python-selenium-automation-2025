from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()

# create a new Chrome browser instance
service = Service(driver_path)
driver: WebDriver = webdriver.Chrome(service=service)
driver.maximize_window()
driver.get('https://www.amazon.com')
driver.find_element(By.CLASS_NAME, 'a-icon a-icon-logo')
driver.find_element(By.ID, 'ap_customer_name')
driver.find_element(By.CSS_SELECTOR, '#ap_email')
driver.find_element(By.CSS_SELECTOR, '#ap_password')
driver.find_element(By.CSS_SELECTOR, '#ap_password_check')