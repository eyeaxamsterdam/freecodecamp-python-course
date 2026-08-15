"""
Step 4
Now you will check whether the user is allowed to book an evening show based on their age.

Create an `if` statement to check if `age` is greater than or equal to `21`. Inside the body of the `if` statement, print `User is eligible for Evening shows`.

Link: https://www.freecodecamp.org/learn/python-v9/workshop-movie-ticket-booking-calculator/step-4
"""

base_price = 15
age = 21
seat_type = 'Gold'
show_time = 'Evening'

if age > 17:
    print('User is eligible to book a ticket')

# --fcc-editable-region--
if age >= 21:
    print('User is eligible for Evening shows')
# --fcc-editable-region--
