Feature: HW-5-SEARCH-PRO-TEST CASES
  #1. Go over your code and remove sleep() wherever possible.
  #Replace sleep() with wait.until if possible.
  #If you can’t remove sleep(), keep it, for example, for target search or opening product details page.
  #
  #2. Review a test case with a loop. Modify it to search for product colors of another product. You can use color selection for any product page you like: it should click on each color and verify that color has been selected.
  #Product examples with multiple colors:


   Scenario: User can search for a product on Target
    Given Open target main pages
    When Search for tea
    Then Verify correct search results show


#search for product colors of another product
