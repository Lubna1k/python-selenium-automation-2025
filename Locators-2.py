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


driver.get("https://www.amazon.com")
#by id
from time import sleep
sleep(2)
#Amazon logo
driver.find_element(By.ID, 'nav-logo-sprites')
#Continue button
driver.find_element(By.ID, 'continue')
#Create your Amazon account button
driver.find_element(By.ID, 'auth-fpp-link-bottom')
#Need help link
driver.find_element(By.XPATH, "//span[@class='a-expander-prompt']")
#Other issues with Sign-In link
driver.find_element(By.ID, 'ap-other-signin-issues-link')
#Create your Amazon account button
driver.find_element(By.ID, 'createAccountSubmit')
#Privacy Notice link
driver.find_element(By.XPATH, "//*[@id='legalTextRow']/a[2]")
#Forgot your password link
driver.find_element(By.XPATH, "//a[contains(@href, 'password?')]")