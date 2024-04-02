"""
Attempt the same bill calculator question 
(Week 1 - Assignment 2 - Q5) but using function. 
Try calling function with different bill amount as a parameter and check the output.
"""


def billDiscountCalculator(bill_amount: float):
    discount: float = 0
    discounted_amount: float = bill_amount
    if bill_amount >= 50000:
        discount = 30
    elif bill_amount >= 40000 and bill_amount < 50000:
        discount = 25
    elif bill_amount >= 30000 and bill_amount < 40000:
        discount = 20
    elif bill_amount >= 10000 and bill_amount < 30000:
        discount = 10

    if discount > 0:
        discounted_amount = bill_amount - (bill_amount * discount / 100)

    print(f"You got {discount}% discount")
    print(f"Your final bill is Rs.{discounted_amount:.2f}")


billDiscountCalculator(60000)
billDiscountCalculator(12000)
