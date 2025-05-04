from unittest import result

from selenium.webdriver.common.by import By
from behave import given, when, then


@when('Search for a {product}')
def search_product(context, product):
    context.driver.find_element(By.ID, 'search').send_keys(product)
    context.driver.find_element(By.CSS_SELECTOR, 'button[data-test="@web/Search/SearchButton"]').click()


@then('Verify {product} is found in the results')
def verify_product_results(context, product):
    actual_result = context.driver.find_element(By.CSS_SELECTOR, '[data-test="lp-resultsCount"] span[class*="h-text-grayDark"]').text
    assert product in actual_result, f'Expected: {product}, but got Actual: {actual_result}'


# @when('user can open find a right {card}')
# def verify_open (context, card):
#     context.driver.find_element(By.ID, '')

@then('Verify {card} is found in the result')
def Verify_card_found(context, card):
     context.driver.find_element(By.CSS_SELECTOR, '[data-test="lp-resultsCoun"]')


