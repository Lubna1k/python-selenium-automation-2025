# Created by lubna khan at 3/30/2025
Feature: # Enter feature name here
  # Enter feature description here

  Scenario: User can add a product to cart
    Given Open Target main page
    When Search for doll
    And Add to cart
    And Confirm Add to cart buton
    And Open cart page
    Then Verify Cart has 1 item(Doll)
    # Enter steps here