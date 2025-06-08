from time import sleep

from selenium.webdriver.common.by import By
from behave import given, when, then

#Target product search
@when('Search for a {product}')
def search_product(context, product):
    context.driver.find_element(By.ID, 'search').send_keys(product)
    context.driver.find_element(By.CSS_SELECTOR, 'button[data-test="@web/Search/SearchButton"]').click()


@then('Verify {product} is found in the results')
def verify_product_results(context, product):
    actual_result = context.driver.find_element(By.CSS_SELECTOR, '[data-test="lp-resultsCount"] span[class*="h-text-grayDark"]').text
    assert product in actual_result, f'Expected: {product}, but got Actual: {actual_result}'

sleep(3)


#------------

# #target circle find right card
#
# @when('user can find a right {card}')
# def verify_open (context, card):
#     context.driver.find_element(By.ID, '$x("//div[@class="cell-item-content"]")')
#
# @when('target circle page')
# def verify_target_circle (context,):
#     context.driver.find_element("https://www.target.com/l/target-circle")
#     #context.driver.find_element(By.XPATH, '$x("//div[@class='cell-item-content"]")')
#
#
#
# @then('Verify {card} is found in the result')
# def Verify_card_found (context, card):
#      context.driver.find_element(By.CSS_SELECTOR, '[data-test="lp-resultsCount"]')
#      context.driver.find_element(By.CLASS_NAME, 'h-text-md')
#      context.driver.find_element(By.ID, '$x("//div[@class="cell-item-content"]")')
# sleep(3)
#
# #target help
# @when('target Help page')
# #def Verify_open_help (context, ):
