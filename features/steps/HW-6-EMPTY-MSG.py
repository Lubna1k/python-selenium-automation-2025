from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@given('Open target main site')
def open_target_main(context):
    context.driver.get('https://www.target.com/')


@when('Click on cart icon')
def click_sign_in(context):
    context.driver.find_element(By.CSS_SELECTOR, "[data-test='@web/CartIcon']").click()
    sleep(3)



@then('Verify cart page opens')
def verify_cart_page_opens(context):
    context.app.cart_page.verify_cart_page_opens()

@then('Verify your cart is empty" message is show')
def verify_cart_is_empty(context):
    actual_text = context.driver.find_element(By.XPATH, "//h1[text()='Your cart is empty']").text
    expected_text = 'Your cart is empty'
    assert expected_text in actual_text, f'Error. Text {expected_text} not in {actual_text}'


# @then("Verify Your cart is 'empty' message is shown")
# def verify_cart_empty(context):
#     expected_result = "Your cart is empty"
#     actual_result = context.driver.find_element(By.CSS_SELECTOR, "[data-test='boxEmptyMsg']").text
#     assert expected_result == actual_result, f'Expected {expected_result} did not match actual {actual_result}'







