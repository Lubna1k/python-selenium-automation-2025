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


@when('user can open find a right {card}')
def verify_open (context, card):
    context.driver.find_element(By.ID )
    #tomorrow i will do it

    # @then('Verify {link_amount} links shown')
    # def verify_all_header_links_shown(context, link_amount):
    #     link_amount = int(link_amount)  # "6" => int 6
    #
    #     links = context.driver.find_elements(*HEADER_LINKS)
    #     print(links)
    #     assert len(links) == link_amount, f'Expected {link_amount} links, but got {len(links)}
    #i will do later