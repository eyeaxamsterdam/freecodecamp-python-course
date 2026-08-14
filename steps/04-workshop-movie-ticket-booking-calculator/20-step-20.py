"""
Step 20
The `if...elif...else` statement is used to check multiple conditions in order.

    if condition1:
       # Code to execute if condition1 is True
    elif condition2:
       # Code to execute if condition1 is False and condition2 is True
    else:
       # Code to execute if all conditions are False

Still inside the body of the outer `if` statement, add an `elif` clause between the `if seat_type == 'Premium':` and `else:` lines and check if `seat_type` is equal to `Gold`. Inside the body of the `elif` clause, update the value of `service_charges` to `3`.

Below the nested `if...elif...else` statement, use the `print()` call to display a message that shows `Service charges:` followed by the updated value of `service_charges`. Then, check the output in the terminal.

Link: https://www.freecodecamp.org/learn/python-v9/workshop-movie-ticket-booking-calculator/step-20
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
if is_weekend or show_time == 'Evening':
    extra_charges = 2
    print('Extra charges will be applied')
else:
    print('No extra charges will be applied')
print('Extra charges:', extra_charges)

if age >= 21 or age >= 18 and (show_time != 'Evening' or is_member):
    print('Ticket booking condition satisfied')

    service_charges = 0
    if seat_type == 'Premium':
        service_charges = 5
# --fcc-editable-region--
    
    else:
        service_charges = 1
# --fcc-editable-region--
else:
    print('Ticket booking failed due to restrictions')
