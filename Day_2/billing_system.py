
# Billing system

def cal_bill(price,quantity,discount):
    total = price * quantity
    final_amount = total - (total * discount/100)
    return final_amount

#use case for POS (point of sales)
bill = cal_bill(price=200, quantity=5, discount=30)
print("Final bill amount will be:", bill)