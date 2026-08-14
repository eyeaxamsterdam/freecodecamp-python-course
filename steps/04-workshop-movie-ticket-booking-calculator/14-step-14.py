"""
Step 14
In Python, the `or` operator is used to check whether at least one of two conditions is true. Here's how you can use it in an `if` statement:

    if condition1 or condition2:
        # Code to execute if any condition is True

Extra charges should also apply if the show is in the evening. Update the condition of the `if is_weekend:` line by using the `or` operator to combine the existing condition with a second condition checking if `show_time` is equal to the string `Evening`.

Link: https://www.freecodecamp.org/learn/python-v9/workshop-movie-ticket-booking-calculator/step-14
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

is_member = False
is_weekend = False

discount = 0
if is_member and age >= 21:
    discount = 3
    print('User qualifies for membership discount')
else:
    print('User does not qualify for membership discount')
print('Discount:', discount)

extra_charges = 0
# --fcc-editable-region--
if is_weekend:
# --fcc-editable-region--
    extra_charges = 2
    print('Extra charges will be applied')
else:
    print('No extra charges will be applied')
print('Extra charges:', extra_charges)
