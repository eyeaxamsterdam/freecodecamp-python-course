"""
Step 9
You should also handle the case when the user does not qualify for a membership discount.

Add an `else` clause to your `if` statement and print `User does not qualify for membership discount` inside the `else` body.

You can print a message followed by a variable like this:

    print('Total:', total)

You also want to display the updated value of `discount`. Below the `if...else` statement, use the `print()` call to display a message that shows `Discount:` followed by the updated value of `discount`. Then, check the output in the terminal.

Link: https://www.freecodecamp.org/learn/python-v9/workshop-movie-ticket-booking-calculator/step-9
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
if is_member:
    discount = 3
    print('User qualifies for membership discount')
# --fcc-editable-region--

# --fcc-editable-region--
