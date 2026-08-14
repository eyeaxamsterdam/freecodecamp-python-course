"""
Step 3
As you learned in previous lessons, in Python, an `if` statement can be used to run code depending on if a condition is true.

An `if` statement consists of the `if` keyword, followed by a condition and a colon. The code to run when the condition is true, which must be indented, is called the body of the `if` statement.

    if condition:
        # Code to execute if condition is True

In this step, you will check if the user is eligible to book a movie ticket based on their age.

Create an `if` statement to check if `age` is greater than `17`. Inside the body of the `if` statement, print `User is eligible to book a ticket`. This will print the message only when the user's age is greater than `17`.

Remember to indent the body of the `if` statement and surround the message with single or double quotes inside the `print()` call.

Link: https://www.freecodecamp.org/learn/python-v9/workshop-movie-ticket-booking-calculator/step-3
"""

base_price = 15
age = 21
seat_type = 'Gold'
show_time = 'Evening'

# --fcc-editable-region--
if age > 17:
    print('User is eligible to book a ticket')    
# --fcc-editable-region--
