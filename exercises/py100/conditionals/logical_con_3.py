# admission_price is 3.99 so print function will print out $3.99
# we are using ternary operator to initialize the value of variable 
# admission_price. Since sale is True, not sale is False.
# admission_price will be 5.25 if not sale evaluates to True.
# If not, the value is 3.99
# in our case, not sale is False. So admission_price was assigned a value 3.99

sale = True
admission_price = 5.25 if not sale else 3.99

print(f"${admission_price}")