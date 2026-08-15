"""
Step 6
Some information can only be true or false. As you have learned in previous lessons, this can be represented using boolean values.

Create a variable named `is_member` to indicate whether the user is a member and set its value to `True`.

Below the `is_member` variable create another variable named `is_weekend` to indicate whether the movie show is on a weekend and sets its value to `False`. Do not surround the value with quotes.

Link: https://www.freecodecamp.org/learn/python-v9/workshop-movie-ticket-booking-calculator/step-6
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

# --fcc-editable-region--
is_member = True
is_weekend = False
# --fcc-editable-region--
