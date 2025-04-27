# Created by lubna khan at 4/24/2025
Feature: homework 6


    # Enter steps here
  Scenario: User can open cart and show message
    Given Open target main page
    When Click on cart icon
    Then Verify Your cart is "empty" message is shown
