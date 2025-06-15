from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@given('Open target main site')
def open_target_main(context):
    context.driver.get("https://www.target.com/")


@when('Click on cart icon')
def click_sign_in(context):
    context.driver.find_element(By.CSS_SELECTOR, "[data-test='@web/CartIcon']").click()
    sleep(3)



@then('Verify cart page opens')
def verify_cart_page_opens(context):
    context.app.cart_page.verify_cart_page_opens()


@then("Verify Your cart is 'empty' message is shown")
def verify_cart_empty(context):
    expected_result = "Your cart is empty"
    actual_result = context.driver.find_element(By.CSS_SELECTOR, "[data-test='boxEmptyMsg']").text
    assert expected_result == actual_result, f'Expected {expected_result} did not match actual {actual_result}'


# HEADER_LINKS = (By.CSS_SELECTOR, "[id*='utilityNav']")
#
#
# @given('Open target main page')
# def open_target_main(context):
#     context.app.main_page.open_main_page()
#
#
# @when('Search for {search_word}')
# def search_product(context, search_word):
#     context.app.header.search(search_word)
#
# @when('Click on Cart icon')
# def click_cart(context):
#     context.app.header.click_cart()
#
# @then('Verify at least 1 link shown')
# def verify_1_header_link_shown(context):
#     link = context.driver.find_element(*HEADER_LINKS)
#     print(link)
#
#
#
#
# @then('Verify {link_amount} links shown')
# def verify_all_header_links_shown(context, link_amount):
#     link_amount = int(link_amount) # "6" => int 6
#     links = context.driver.find_elements(*HEADER_LINKS)
#     print(links)
#     assert len(links) == link_amount, f'Expected {link_amount} links, but got {len(links)}'





