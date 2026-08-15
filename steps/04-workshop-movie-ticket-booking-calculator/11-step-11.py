"""
Step 11
Now change the value of the `is_member` variable to `False` as the user is not a member.

After that, you will see that the `discount` value now remains `0`, because both conditions must be satisfied for the discount to apply.

Link: https://www.freecodecamp.org/learn/python-v9/workshop-movie-ticket-booking-calculator/step-11
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
is_member = False 
# --fcc-editable-region--
is_weekend = False

discount = 0
if is_member and age >= 21:
    discount = 3
    print('User qualifies for membership discount')
else:
    print('User does not qualify for membership discount')
print('Discount:', discount)
