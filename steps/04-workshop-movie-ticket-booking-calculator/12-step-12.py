"""
Step 12
Now create a variable named `extra_charges` and set it to `0`. This will represent extra charges to apply to the movie ticket on weekends.

Then, create an `if` statement to check if `is_weekend` is truthy. Inside the body of `if` statement, update the `extra_charges` value to `2` and print `Extra charges will be applied` in the terminal.

Link: https://www.freecodecamp.org/learn/python-v9/workshop-movie-ticket-booking-calculator/step-12
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

# --fcc-editable-region--

# --fcc-editable-region--
