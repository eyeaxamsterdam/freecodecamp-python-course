"""
Step 5
In the previous step, you checked a condition using an `if` statement. The `else` clause is used to handle the case when the condition is false. Here's the syntax of an `if...else` statement:

    if condition:
        # Code to execute if condition is True
    else:
        # Code to execute if condition is False

Now, add an `else` clause to your `if` statement and print `User is not eligible for Evening shows` inside the `else` body. This will print only when the condition in the `if` statement is false.

Link: https://www.freecodecamp.org/learn/python-v9/workshop-movie-ticket-booking-calculator/step-5
"""

base_price = 15
age = 21
seat_type = 'Gold'
show_time = 'Evening'

if age > 17:
    print('User is eligible to book a ticket')

if age >= 21:
    print('User is eligible for Evening shows')
# --fcc-editable-region--
else:
    print('User is not eligible for Evening shows')
# --fcc-editable-region--
