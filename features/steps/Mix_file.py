# Verify Links-LUBNA
#@given('target circle page')
#def open_target(context):
   # context.driver.get('https://www.target.com/circle')
    #context.driver.get('https://www.target.com/l/target-circle/-/N-pzno9')


#@when('Verify {links_here}')
#def verify_links_here(context, links_here):
  ##  links = context.driver.find_elements(*CIRCLE_LINKS)
   # assert len(links) == int(links_here), f"Expected {links_here} links, got {len(links_here)}"



# @when('find {find_links}')
# def verify_links(context, find_links):
#     context.driver.find_element(*SEARCH_FIELD).send_keys(find_links)
#     context.driver.find_element(*SEARCH_BUTTON).click()
#     sleep(2)
#
# @then('Verify page has {10_benefit_cell}')
# def Verify_page_10_cell(context, cell):
#     context.driver.find_element("cell-item-content")
#     assert len("cell-item-content")




# @when('Add to cart')
# def add_to_cart(context):
#     context.driver.find_element(By.CSS_SELECTOR, "[data-test='orderPickupButton'][id*='addToCartButton']").click()
#     sleep(2)
#     context.driver.find_element(By.CSS_SELECTOR, "[data-test*='orderPickupButton']").click()
#     sleep(2)
#     context.driver.find_element(By.XPATH, "//a[text()='View cart & check out']").click()
#     sleep(2)
#     context.driver.find_element(By.CSS_SELECTOR, "[data-test='cart-order-summary']").text('total')