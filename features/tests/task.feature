Feature: User Story "Create Task"


  Scenario: Verify 'My Tasks' link on the NavBar
    Given Open Sign in page
    When Enter Email
    When Enter Password
    Then Sign In
    Then Verify My Tasks link


  Scenario: Verify that clicking on 'My Task' link will redirect user to a page with tasks
    Given Open Sign in page
    When Enter Email
    When Enter Password
    Then Sign In
    When Click on My Tasks link
    Then Verify the task page


  Scenario: Verify displayed message
    Given Open Sign in page
    When Enter Email
    When Enter Password
    Then Sign In
    When Click on My Tasks link
    Then Verify displayed message


  Scenario: Verify that user is able to create a task
    Given Open Sign in page
    When Enter Email
    When Enter Password
    Then Sign In
    When Click on My Tasks link
    When Enter task ABCDE name
    When Click plus
    Then Verify that new task created


  Scenario: Verify that user unable to create 2 characters task name
    Given Open Sign in page
    When Enter Email
    When Enter Password
    Then Sign In
    When Click on My Tasks link
    When Enter two characters task name
    When Click plus
    Then Verify two characters task name not created


  Scenario: Verify that task can't have more than 250 characters
    Given Open Sign in page
    When Enter Email
    When Enter Password
    Then Sign In
    When Click on My Tasks link
    When Enter two fifty one characters task name
    When Click plus
    Then Verify two fifty one characters task name not created



