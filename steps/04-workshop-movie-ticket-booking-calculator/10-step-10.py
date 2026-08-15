"""
Step 10
In Python, the `and` operator is used to check if multiple conditions are true. Here's how you can use it to combine two conditions in an `if` statement:

    if condition1 and condition2:
        # Code to execute if all conditions are True

The membership discount should only apply to members if their `age` is greater than or equal to `21`.

Update the condition of the `if is_member:` line by using the `and` operator to combine the existing condition with another condition checking if `age` is greater than or equal to `21`.

Link: https://www.freecodecamp.org/learn/python-v9/workshop-movie-ticket-booking-calculator/step-10
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
# --fcc-editable-region--
    discount = 3
    print('User qualifies for membership discount')
else:
    print('User does not qualify for membership discount')
print('Discount:', discount)