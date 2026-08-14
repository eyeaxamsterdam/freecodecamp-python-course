"""
Step 21
In this final step, you will calculate the final price of the movie ticket using the values calculated in the previous steps.

The final ticket price is calculated by adding the extra charges and service charges to the base price, and then subtracting the discount.

Inside the body of the last `if` statement, below the `print('Service charges:', service_charges)` line, calculate the final price of the ticket and store it in a variable named `final_price`.

Finally, print a message that shows `Final price of ticket:` followed by the value of `final_price`.

Link: https://www.freecodecamp.org/learn/python-v9/workshop-movie-ticket-booking-calculator/step-21
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
    elif seat_type == 'Gold':
        service_charges = 3
    else:
        service_charges = 1
    print('Service charges:', service_charges)

# --fcc-editable-region--
    
# --fcc-editable-region--
else:
    print('Ticket booking failed due to restrictions')
