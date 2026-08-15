"""
Step 7
The user qualifies for a membership discount if they are a member.

Create a variable named `discount` and set its value to `0`. This will store the discount the user gets on the movie ticket.

Link: https://www.freecodecamp.org/learn/python-v9/workshop-movie-ticket-booking-calculator/step-7
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

# --fcc-editable-region--
discount = 0
# --fcc-editable-region--
