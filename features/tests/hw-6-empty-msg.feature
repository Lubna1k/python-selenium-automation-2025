# Created by lubna khan at 4/24/2025
Feature: homework 6

  #Scenario: “Your cart is empty” message is shown for empty cart
  #Open target.com
  #Click on Cart icon
  #Verify “Your cart is empty” message is shown

    # Enter steps here
  Scenario: Your cart is empty” message is shown for empty cart
    Given Open target main site
    When Click on cart icon
    Then Verify cart page opens
    Then Verify Your cart is 'empty' message is shown
