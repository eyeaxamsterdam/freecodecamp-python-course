"""
Step 8
In Python, `if` conditions don't have to compare values explicitly to `True` or `False`. Instead, they rely on the truthiness of values. Truthy values evaluate to `True` in a boolean context, such as the condition of an `if` statement. These include non-zero numbers, non-empty strings, and the boolean value `True`.

    if value:
       print('value is truthy')

Create an `if` statement to check if `is_member` is truthy. Inside the body of the `if` statement, update the `discount` value to `3` and print `User qualifies for membership discount` to the terminal.

Link: https://www.freecodecamp.org/learn/python-v9/workshop-movie-ticket-booking-calculator/step-8
"""

base_price = 15
age = 21
seat_type = 'Gold'
show_time = 'Evening'

if age > 17:
    print('User is eligible to book a ticket')

if age >= 21:
    print('User is eligible for Evening shows')
else:
    print('User is not eligible for Evening shows')

is_member = True
is_weekend = False

discount = 0
# --fcc-editable-region--
if is_member:
    discount = 3
    print('User qualifies for membership discount')    
# --fcc-editable-region--
