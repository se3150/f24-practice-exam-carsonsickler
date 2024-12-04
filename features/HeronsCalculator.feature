Feature: calculate the area of a triangle
As an aspiring mathematician
I should be able to calculate the area of a triangle
So that I can chat with my math friends like a pro

Scenario: I can calculate the area of a triangle
    Given I open the site "https://byjus.com/herons-calculator/"
    # write your steps here
    When I enter the sides of the triangle as 3, 4, 5
    And I click on the element "input.clcbtn"
    Then I should see the area of the triangle as 6

