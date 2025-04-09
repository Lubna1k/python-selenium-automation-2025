import when
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

driver.find_element(By.ID, 'search')
driver.find_element(By.ID, "searchMobile")


def input_search(context):
    context.driver.find_element(By.ID, 'twotabsearchtextbox').send_keys('DOLL')

    def search_icon(context):
        context.driver.find_element(By.CSS_SELECTOR, '#nav-search-submit-button').click()

        context.driver.find_element(By.CSS_SELECTOR, "span.a-price-whole").click()

        context.driver.find_element(By.ID, 'add-to-cart-button').click()

        context.driver.find_element(By.CSS_SELECTOR,
 '.a-button-input[name=proceedToRetailCheckout]').is_displayed(), f'checkout button does not appear'