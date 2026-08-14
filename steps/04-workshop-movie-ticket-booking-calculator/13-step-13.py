"""
Step 13
Now, add an `else` clause to your `if` statement and print `No extra charges will be applied` inside the `else` body. This will print the message only when the extra charges condition is false.

Then, below the `else` clause, use the `print()` call to display a message that shows `Extra charges:` followed by the updated value of `extra_charges` and check the output in the terminal.

Link: https://www.freecodecamp.org/learn/python-v9/workshop-movie-ticket-booking-calculator/step-13
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
if is_weekend:
    extra_charges = 2
    print('Extra charges will be applied')
# --fcc-editable-region--

# --fcc-editable-region--
