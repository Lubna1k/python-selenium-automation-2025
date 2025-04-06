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
driver.get('https://www.target.com/l/target-circle/-/N-pzno9')
#driver.find_element(By.ID 'h-text-md')

from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

CIRCLE_LINKS = (By.CSS_SELECTOR, "[id*='altlmH4']")
SEARCH_FIELD = (By.ID, 'search')
SEARCH_BUTTON = (By.CSS_SELECTOR, "[data-test='@web/Search/SearchButton'")
# SEARCH_INPUT = (By.NAME, 'q')
# SEARCH_SUBMIT = (By.NAME, 'btnK')


# Verify Links---

@given('Open Target Circle page')
def open_target(context):
    context.driver.get('https://www.target.com/l/target-circle/-/N-pzno9')

@then('Verify {link_amount} links')
def verify_links(context, link_amount):
    links = context.driver.find_elements(*CIRCLE_LINKS)
    assert len(links) == int(link_amount), f"Expected {link_amount} links, got {len(links)}"


# Search product and add to cart

@given('Open Target main page')
def open_target_main_page(context):
    context.driver.get('https://www.target.com')


@when('search for {search_word}')
def verify_links(context, search_word):
    context.driver.find_element(*SEARCH_FIELD).send_keys(search_word)
    context.driver.find_element(*SEARCH_BUTTON).click()
    sleep(2)


@when('Add to cart')
def add_to_cart(context):
    context.driver.find_element(By.CSS_SELECTOR, "[data-test='orderPickupButton'][id*='addToCartButton']").click()
    sleep(2)
    context.driver.find_element(By.CSS_SELECTOR, "[data-test*='orderPickupButton']").click()
    sleep(2)
    context.driver.find_element(By.XPATH, "//a[text()='View cart & check out']").click()
    sleep(2)
    context.driver.find_element(By.CSS_SELECTOR, "[data-test='cart-order-summary']").text('total')