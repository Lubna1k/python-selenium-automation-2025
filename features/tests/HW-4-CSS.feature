# Created by lubna khan at 3/30/2025
Feature: User can open target.com/circle
  # Enter feature description here

  Scenario: Target product search
    Given Open Target main page
    When Search for a table
    Then Verify table is found in the results

  Scenario: target circle find a right Card
    Given open target circle page
    When Verify open right card
    Then Verify Card is found

#  Scenario: user can open find a right card for you
#    Given open Target Circle Page
#    Then Verify there are 6 benefit boxes



    # Enter steps here

#  Feature: Test Scenarios for Search functionality
#
##  Scenario: User can search for a product
##    Given Open Google page
##    When Input Car into search field
##    And Click on search icon
##    Then Product results for Car are shown