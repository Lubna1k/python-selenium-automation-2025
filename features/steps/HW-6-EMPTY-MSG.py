from behave.reporter.summary import status_order
from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep



@when('Click Sign In')
def click_sign_in(context):
    context.driver.find_element(By.CSS_SELECTOR, "[data-test='@web/AccountLink']").click()
    sleep(5)

@when('click Sign In side menu')
def click_sign_in_side_menu(context):
    context.driver.find_element(By.CSS_SELECTOR, "[data-test='accountNav-signIn']").click()
    sleep(6)


@then('Verify Sign In form opened')
def verify_sign_in_form(context):
    actual_text = context.driver.find_element(By.XPATH, "//h1[contains(@class, 'styles_ndsHeading')]").text
    expected_text = 'Sign in'
    assert expected_text in actual_text, f'Error. Text {expected_text} not in {actual_text}'


@then('Verify Your cart is "empty" message is shown')
def verify_cart_empty(context):
    expected_result = 'Your cart is empty'
    actual_result = context.driver.find_element(By.CSS_SELECTOR, "[data-test='boxEmptyMsg']").text
    assert expected_result == actual_result, f'Expected {expected_result} did not match actual {actual_result}'



