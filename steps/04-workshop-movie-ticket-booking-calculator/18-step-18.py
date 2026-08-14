"""
Step 18
In Python, an `if` statement can also be placed inside the body of another `if` statement. This is called a nested `if` statement.

A nested `if` statement allows you to check an additional condition only after the first condition has already been satisfied. The inner `if` statement will run only if the outer `if` condition is true.

    if condition1:
        # Code to execute if condition1 is True
        if condition2:
            # Code to execute if both conditions are True

Now you will calculate service charges based on the type of seat the user has selected.

Inside the body of the last `if` statement, below the `print('Ticket booking condition satisfied')` line, create a variable named `service_charges` and set it to `0`. Make sure to indent your code by four spaces to keep it inside the outer `if` statement body.

Then, create a nested `if` statement to check if `seat_type` is equal to `Premium`. Inside the body of the nested `if` statement, update the `service_charges` value to `5`.

Link: https://www.freecodecamp.org/learn/python-v9/workshop-movie-ticket-booking-calculator/step-18
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

# --fcc-editable-region--
    
# --fcc-editable-region--
else:
    print('Ticket booking failed due to restrictions')
