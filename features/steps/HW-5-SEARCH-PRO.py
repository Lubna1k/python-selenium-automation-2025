from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

@given('Open target main page')
def open_target_main(context):
    context.driver.get('https://www.target.com/')
    sleep(6)
@when('Search for tea')
def search_product(context):
    context.driver.find_element(By.ID, 'search').send_keys('tea')
    context.driver.find_element(By.XPATH, "//button[@data-test='@web/Search/SearchButton']").click()
    sleep(6)



#@then('Verify correct search results show')
# @given('Open target')
# def open_target_main(context):
#     context.driver.get('https://www.target.com/')
#
# @when('search for mug')
# def search_product(context):
#     context.driver.find_element(By.XPATH, "//button[@data-test='@web/Search/SearchButton']").click()
#     sleep(6)