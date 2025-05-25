from behave.model import Scenario
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

#target circle find right card

# @when('user can find a right {card}')
# def verify_open (context, card):
#     context.driver.find_element(By.ID, '$x("//div[@class="cell-item-content"]")')
#
# @when('target circle page')
# def verify_target_circle (context, card):
#     context.driver.find_element("https://www.target.com/l/target-circle")
#
#
#
#  @then('Verify {card} is found in the result')
# def Verify_card_found (context, card):
#      context.driver.find_element(By.CSS_SELECTOR, '[data-test="lp-resultsCoun"]')
#      context.driver.find_element(By.CLASS_NAME, 'h-text-md')
#
#    # context.driver.find_element(By.CSS_SELECTOR, '$x("//a[text()='Find a card right for you']")')
#
#
#    #---
# SEARCH_RESULTS_TEXT = (By.XPATH, "//div[@data-test='lp-resultsCount']")
# ADD_TO_CART_BTN = (By.CSS_SELECTOR, "[id*='addToCartButton']")
# SIDE_NAV_PRODUCT_NAME = (By.CSS_SELECTOR, "[data-test='content-wrapper'] h4")
# SIDE_NAV_ADD_TO_CART_BTN = (By.CSS_SELECTOR, "[data-test='content-wrapper'] [id*='addToCart']")
#
#
# @when('Click on Add to Cart button')
# def click_add_to_cart(context):
#     context.driver.find_element(*ADD_TO_CART_BTN).click()  # always clicks on 1st Add to cart btn
#
#
# @when('Store product name')
# def store_product_name(context):
#   context.driver.wait.until(
# EC.visibility_of_element_located(SIDE_NAV_PRODUCT_NAME),
# message='Product name not visible')
#   context.product_name = context.driver.find_element(*SIDE_NAV_PRODUCT_NAME).text
#   print('Product name stored: ', context.product_name)
#
#
#  @when('Confirm Add to Cart button from side navigation')
# def side_nav_click_add_to_cart(context):
#   context.driver.find_element(*SIDE_NAV_ADD_TO_CART_BTN).click()
#
# @then('Verify correct search results shown for {expected_text}')
# def verify_search_results(context, expected_text):
#     actual_text = context.driver.find_element(*SEARCH_RESULTS_TEXT).text
#
#     assert expected_text in actual_text, f'Error. Text {expected_text} not in {actual_text}'




