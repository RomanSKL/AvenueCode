Feature: User Story "Create SubTask"


  Scenario: Verify a button labeled as 'Manage Subtasks' opens modal dialog
    Given Open Sign in page
    When Enter Email
    When Enter Password
    Then Sign In
    When Click on My Tasks link
    When Enter task SKL name
    When Click plus
    When Click a button labeled as Manage Subtasks
    Then Verify modal dialog


  Scenario: Verify that button 'Manage Subtasks' has the number of subtasks
    Given Open Sign in page
    When Enter Email
    When Enter Password
    Then Sign In
    When Click on My Tasks link
    When Enter task AUTO name
    When Click plus
    Then Verify button Manage Subtasks has the number of subtasks


  Scenario: Verity pop up window has task ID and task description
    Given Open Sign in page
    When Enter Email
    When Enter Password
    Then Sign In
    When Click on My Tasks link
    When Enter task AVENUECODE name
    When Click plus
    When Click a button labeled as Manage Subtasks
    Then Verify task ID
    Then Verify task description
    Then Verify SubTask due date (MM/dd/yyyy format)


  Scenario: Verify that user can enter SubTask Description (250 characters)
    Given Open Sign in page
    When Enter Email
    When Enter Password
    Then Sign In
    When Click on My Tasks link
    When Enter task ZERO name
    When Click plus
    When Click a button labeled as Manage Subtasks
    When Enter TWO FIFTY SubTask Description
    When Click add subtask
    Then Verify TWO FIFTY subtask created


  Scenario: Verify Task Description and Due Date are required fields
    Given Open Sign in page
    When Enter Email
    When Enter Password
    Then Sign In
    When Click on My Tasks link
    When Enter task DATA name
    When Click plus
    When Click a button labeled as Manage Subtasks
    When Click add subtask
    Then Verify Task Description and Due Date are required fields

