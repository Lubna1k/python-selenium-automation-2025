# Created by lubna khan at 5/4/2025
Feature: HW-6-PAGE-OB
  # Enter feature description here

  Scenario:Scenario: User can open cart and show message
    Given Open target main page header
    When Click on cart icon header
    Then Verify Your cart is "empty" message is shown