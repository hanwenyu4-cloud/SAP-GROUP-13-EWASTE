print("-"*85)
print("PAYMENT METHOD".center(80))
print("-"*85)

payment_method = input("Enter your payment method(TNG/BANK):").upper()
if payment_method == "TNG":
  phone_num = int(input("Enter your phone number(Type it without"-"): "))
elif payment_method == "BANK":
  bank = input("Enter preferred bank: ")
  account_number = int(input("Enter bank account number: "))
else:
  print("Invalid payment method")

print("Email sent to the user's email.")
print("="*85)
print ("RECEIPT".center(80))
print("="*85)
print("Name: ",name)
print("Email: ",email)
print("-"*85)
print("Device Type : (1)Smartphone, (2)Laptop, (3)Tablet")
print("Device Type: ",devicetype)
print("Device Brand: ",brand)
print("Price: ",price)
print("="*85)
print("THANK YOU!".center(80))
print("SERVICE WILL BE DONE IN 3 WORKING DAYS")