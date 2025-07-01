from selenium.webdriver.common.by import By
from behave import  given,when,then
from time import sleep


CIRCLE_LINKS = (By.CSS_SELECTOR, "[id*='altlmH4']")
SEARCH_FIELD = (By.ID, 'search')
SEARCH_BUTTON = (By.CSS_SELECTOR, "[data-test='@web/Search/SearchButton")
SEARCH_INPUT = (By.NAME, 'q')
SEARCH_SUBMIT = (By.NAME, 'btnK')

@given("I am on the Target Circle page")
def step_impl(context):
    context.driver.get("https://www.target.com/circle")



@then("Verify page is correct")
def verify_page(context):
    context.driver.get("https://www.target.com/circle")


@when('user click on circle btn')
def click_0n_circle(context):
    context.driver.find_element(By.XPATH, "//div[@class='cell-item-content']").click()
    sleep(3)




