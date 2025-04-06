from multiprocessing import context

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
sleep(5)
driver.get('https://www.target.com/')
@given('Store original window')
def store_original_window(context):
    context.original_window = context.app.base_page.get_current_window_handle()
    print('Original_window:', context.original_window)

@then('Close current page')

def close_page(context):
    context.app.base_page.close()

@then('Return to original window')
def switch_to_original_window(context):
    context.app.base_page.switch_to_window_by_id(context.original_window)