product = float("Enter the name of the product : ")
price = int(input("Enter the price for the product(Q-1): "))
quantity = int(input("Enter the quantity of the product : "))
total_price = price*quantity
if quantity >= 20 :
    print("The discount will be applied to the product!")
    discount = 0.20
elif quantity >= 15 :
    print("The discount will be applied partially.")
    discount =  0.10
else:
    print("The discount will NOT be applied to the product.")
    discount = 0.00
discount_amount  = total_price*discount
final_price = total_price - discount_amount
print(f"The discount applied is : {discount_amount}.")
print(f"The final price is {final_price}.")
