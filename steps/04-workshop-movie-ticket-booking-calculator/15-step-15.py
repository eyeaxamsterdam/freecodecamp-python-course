"""
Step 15
Now you will check if the user satisfies the conditions to book a movie ticket. Users with age `21` or above can always book tickets without any restrictions.

Create an `if` statement to check if `age` is greater than or equal to `21`. Inside the body of the `if` statement, print `Ticket booking condition satisfied` to the terminal.

Then, add an `else` clause to your `if` statement and print `Ticket booking failed due to restrictions` inside the `else` body.

Link: https://www.freecodecamp.org/learn/python-v9/workshop-movie-ticket-booking-calculator/step-15
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

# --fcc-editable-region--

# --fcc-editable-region--
