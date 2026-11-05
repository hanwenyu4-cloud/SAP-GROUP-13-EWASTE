# SMART E-WASTE PHONE MANAGEMENT 2050
print("_" * 85)
print("SMART E-WASTE PHONE MANAGEMENT 2050".center(85))
print("")
print("Welcome New User".center(85))
print("_" * 85)
print("")

# -------------------- USER REGISTRATION --------------------
name = str(input("Username: "))
email = str(input("Email: "))
confirmemail = str(input("Confirmed Email: "))

while confirmemail != email:
    print("Invalid")
    print("Please recheck email.")
    print("")
    name = str(input("Username: "))
    email = str(input("Email: "))
    confirmemail = str(input("Confirmed Email: "))

# -------------------- NUMBER OF DEVICES --------------------
print("")
print("=" * 85)
numdevice = int(input("Number of Device to Store: "))
print("=" * 85)
print("")

# -------------------- FUNCTIONS --------------------
def calculate_device_value(battery_life, mass_in_g, recycable_percentage):
    if battery_life <= 50:
        value_price = mass_in_g * recycable_percentage * 0.5
    elif battery_life <= 70:
        value_price = mass_in_g * recycable_percentage * 0.7
    elif battery_life <= 85:
        value_price = mass_in_g * recycable_percentage * 0.85
    elif battery_life <= 95:
        value_price = mass_in_g * recycable_percentage * 0.95
    else:
        value_price = mass_in_g * recycable_percentage
    print("Estimated Value of Device:  RM", round(value_price,2))
    return value_price

count = 1
total_price = 0

while count <= numdevice:
    print("")
    print("(1)Smartphone")
    print("(2)Laptop")
    print("(3)Tablet")
    devicetype = int(input("Choose Device Type: "))
    value_price = 0.0  

    if devicetype == 1:
        os = str(input("Operating System: "))    
        brand = str(input("Brand: "))
        model = str(input("Device Model: "))
        
        if brand.upper() == "APPLE":
            ios_model = str(input("IOS Model: "))
            time_not_used = int(input("MONTHS: "))
            battery_life = float(input("Battery Life (%): "))
          
            print("")
            print("Select Your Choice:")
            print("(1) Store")
            print("(2) Recycle")
            if battery_life <= 85:
                print("RECYCLE is Recommended.")
            choice = int(input("Decide your next action: "))

            if choice == 1:
                value_price = 0.0
                print("Device registered for storage. No payout issued.")
              
            elif choice == 2:
                if model.upper() == "IPHONE 17":
                    recycable_percentage = 0.3
                    mass_in_g = 177
                    value_price = calculate_device_value(battery_life, mass_in_g, recycable_percentage)
        
        elif brand.upper() in {"SAMSUNG", "HUAWEI", "OPPO", "HONOR", "VIVO", "ROG", "XIAOMI", "REALME", "SONY", "NOKIA", "LENOVO"}:
            android_model = str(input("ANDROID Model: "))
            time_not_used = int(input("MONTHS: "))
            battery_type = str(input("Enter battery type (LI-ION / LI-PO / SILICON-CARBON): ")).upper()
            battery_condition = str(input("Enter battery's condition (working = W) (not working = NW): "))
            motherboard_type = str(input("Enter motherboard's condition (working = W) (not working = NW): "))
            frame_type = str(input("What's the frame type? : "))

            if battery_type == "LI-ION":
                value_price = 90 - time_not_used * 0.20
            elif battery_type == "LI-PO":
                value_price = 70 - time_not_used * 0.20
            elif battery_type == "SILICON-CARBON":
                value_price = 50 - time_not_used * 0.20
            else:
                value_price = 40 - time_not_used * 0.20

            print("")
            print("Select Your Choice:")
            print("(1) Store")
            print("(2) Recycle")
            if time_not_used > 24:
                print("RECYCLE is Recommended.")
            choice = int(input("Decide your next action: "))

            if choice == 1:
                value_price = 0.0
                print("Device registered for storage. No payout issued.")
              
            elif choice == 2:
                print("Estimated Value of Device:  RM", round(value_price,2))
              
            else:
                print("Invalid choice! Only enter '1' or '2'.")
                exit()
              
    elif devicetype == 2:
        brand = str(input("Brand: "))
        model = str(input("Device Model: "))
        
        if brand.upper() == "APPLE":
            ios_model = str(input("IOS Model: "))
            time_not_used = int(input("MONTHS: "))
            battery_life = float(input("Battery Life (%): "))

            print("")
            print("Select Your Choice:")
            print("(1) Store")
            print("(2) Recycle")
            if battery_life <= 85:
                print("RECYCLE is Recommended.")
            choice = int(input("Decide your next action: "))

            if choice == 1:
                value_price = 0.0
                print("Device registered for storage. No payout issued.")
              
            elif choice == 2:
                if model.upper() == "MACBOOK AIR M4":
                    recycable_percentage = 0.3
                    mass_in_g = 177
                    value_price = calculate_device_value(battery_life, mass_in_g, recycable_percentage)
                  
            else:
                print("Invalid choice! Only enter '1' or '2'.")
                exit()
      
        elif brand.upper() in {"HP", "ROG", "ASUS", "REALME", "SONY", "MSI", "LENOVO"}:
            windows_model = str(input("Windows Model: "))  
            time_not_used = int(input("MONTHS: "))
            
            print("")
            print("Select Your Choice:")
            print("(1) Store")
            print("(2) Recycle")
            if time_not_used >= 36:
                print("RECYCLE is Recommended.")
                
            choice = int(input("Decide your next action: "))
            print("")

            if choice == 1:
                value_price = 0.0
                print("Device registered for storage. No payout issued.")
              
            elif choice == 2:
                motherboard_type = (input("Enter motherboard's condition (working = W) (not working = NW): ")).upper()
                if motherboard_type == "NW":
                    motherboard_mass = float(input("Enter motherboard's mass (g): "))
                    price_motherboard = motherboard_mass * 0.03
                elif motherboard_type == "W": 
                    grade = input("Enter type of motherboard (Legacy = L / Basic = B / Mainstream = M / Gaming = G / Premium = P): ").upper()
                    if grade == "L": price_motherboard = 50
                    elif grade == "B": price_motherboard = 150
                    elif grade == "M": price_motherboard = 275
                    elif grade == "G": price_motherboard = 400
                    elif grade == "P": price_motherboard = 700
                    else: price_motherboard = 50

                battery_condition = input("Enter battery's condition (working = W) (not working = NW): ").upper()
                if battery_condition == "W":
                    battery_grade = input("Enter grade of battery (A/B/C): ").upper()
                    if battery_grade == "A": price_battery = 200
                    elif battery_grade == "B": price_battery = 100
                    elif battery_grade == "C": price_battery = 50
                    else: price_battery = 50
                elif battery_condition == "NW":
                    battery_mass = float(input("Enter battery's mass (g): "))
                    price_battery = battery_mass * 0.0027

                frame_type = input("Enter type of frame (plastic/polypropylene/mix/metal): ").lower()
                frame_mass = float(input("Enter mass of frame (kg): "))
                if frame_type == "plastic": price_frame = frame_mass * 0.83
                elif frame_type == "polypropylene": price_frame = frame_mass * 1.00
                elif frame_type == "mix": price_frame = frame_mass * 0.25
                elif frame_type == "metal": price_frame = frame_mass * 8
                else: price_frame = frame_mass * 0.5     

                value_price = price_motherboard + price_battery + price_frame 
                print("Estimated Value of Device:  RM", round(value_price,2))
              
            else:
              print("Invalid choice! Only enter '1' or '2'.")
              exit()
              
        elif brand.upper() in {"HUAWEI", "OPPO", "VIVO", "SAMSUNG"}:
            android_model = str(input("ANDROID Model: "))
            time_not_used = int(input("MONTHS: "))

            print("")
            print("Select Your Choice:")
            print("(1) Store")
            print("(2) Recycle")
            if time_not_used >= 36:
                print("RECYCLE is Recommended.")
            choice = int(input("Decide your next action: "))
            print("")

            if choice == 1:
                value_price = 0.0
                print("Device registered for storage. No payout issued.")
              
            elif choice == 2:
                motherboard_type = (input("Enter motherboard's condition (working = W) (not working = NW): ")).upper()
                if motherboard_type == "NW":
                    motherboard_mass = float(input("Enter motherboard's mass (g): "))
                    price_motherboard = motherboard_mass * 0.03
                  
                elif motherboard_type == "W": 
                    grade = input("Enter type of motherboard (Legacy = L / Basic = B / Mainstream = M / Gaming = G / Premium = P): ").upper()
                    if grade == "L": price_motherboard = 50
                    elif grade == "B": price_motherboard = 150
                    elif grade == "M": price_motherboard = 275
                    elif grade == "G": price_motherboard = 400
                    elif grade == "P": price_motherboard = 700
                    else: price_motherboard = 50

                battery_condition = input("Enter battery's condition (working = W) (not working = NW): ").upper()
                if battery_condition == "W":
                    battery_grade = input("Enter grade of battery (A/B/C): ").upper()
                    if battery_grade == "A": price_battery = 200
                    elif battery_grade == "B": price_battery = 100
                    elif battery_grade == "C": price_battery = 50
                    else: price_battery = 50
                      
                elif battery_condition == "NW":
                    battery_mass = float(input("Enter battery's mass (g): "))
                    price_battery = battery_mass * 0.0027

                frame_type = input("Enter type of frame (plastic / polypropylene / mix / metal): ").lower()
                frame_mass = float(input("Enter mass of frame (kg): "))
                if frame_type == "plastic": price_frame = frame_mass * 0.83
                elif frame_type == "polypropylene": price_frame = frame_mass * 1.00
                elif frame_type == "mix": price_frame = frame_mass * 0.25
                elif frame_type == "metal": price_frame = frame_mass * 8
                else: price_frame = frame_mass * 0.5

                value_price = price_motherboard + price_battery + price_frame 
                print("Estimated Value of Device:  RM", round(value_price,2))
              
            else:
              print("Invalid choice! Only enter '1' or '2'.")
              exit()
        
    elif devicetype == 3:
      brand = str(input("Brand: "))
      model = str(input("Device Model: "))
      
      if brand.upper() == "APPLE":
          ios_model = str(input("IOS Model: "))
          time_not_used = int(input("MONTHS: "))
          battery_life = float(input("Battery Life (%): "))
        
      elif brand.upper() in {"SAMSUNG", "HUAWEI", "OPPO", "HONOR", "VIVO", "ROG", "XIAOMI", "REALME", "SONY", "LENOVO"}:
          android_model = str(input("ANDROID Model: "))    
          time_not_used = int(input("MONTHS: "))
            
      print("")
      print("Select Your Choice:")
      print("(1) Store")
      print("(2) Recycle")
  
      if time_not_used >= 36:
          print("RECYCLE is Recommended.")
  
      choice = int(input("Decide your next action: "))
          
      if choice == 1:
          value_price = 0.0
          print("Device registered for storage. No payout issued.")
        
      elif choice == 2:
          print("")
          print("MOTHERBOARD INFORMATION")
          motherboard_type = input("Enter motherboard's condition (working = W) (not working = NW): ").upper()
  
          if motherboard_type == "NW":
              motherboard_mass = float(input("Enter motherboard's mass (g): "))
              price_motherboard = motherboard_mass * 0.03
            
          elif motherboard_type == "W":
              grade = input("Enter type of motherboard (Legacy = L / Basic = B / Mainstream = M / Gaming = G / Premium = P): ").upper()
              if grade == "L": price_motherboard = 50
              elif grade == "B": price_motherboard = 150
              elif grade == "M": price_motherboard = 275
              elif grade == "G": price_motherboard = 400
              elif grade == "P": price_motherboard = 700
              else: price_motherboard = 50
  
          print("")
          print("BATTERY INFORMATION")
          battery_condition = input("Enter battery's condition (working = W) (not working = NW): ").upper()
  
          if battery_condition == "W":
              battery_grade = input("Enter grade of battery (A/B/C): ").upper()
              if battery_grade == "A": price_battery = 200
              elif battery_grade == "B": price_battery = 100
              elif battery_grade == "C": price_battery = 50
              else: price_battery = 50
                
          elif battery_condition == "NW":
              battery_mass = float(input("Enter battery's mass (g): "))
              price_battery = battery_mass * 0.0027
  
          print("")
          print("FRAME INFORMATION")
          frame_type = input("Enter type of frame (plastic / polypropylene / mix / metal): ").lower()
          frame_mass = float(input("Enter mass of frame (kg): "))
  
          if frame_type == "plastic": price_frame = frame_mass * 0.83
          elif frame_type == "polypropylene": price_frame = frame_mass * 1.00
          elif frame_type == "mix": price_frame = frame_mass * 0.25
          elif frame_type == "metal": price_frame = frame_mass * 8
          else: price_frame = frame_mass * 0.5
  
          value_price = price_motherboard + price_battery + price_frame
  
          print("")
          print("=" * 50)
          print("TABLET RECYCLING VALUATION".center(50))
          print("=" * 50)
          print("Motherboard Value: RM", round(price_motherboard, 2))
          print("Battery Value: RM", round(price_battery, 2))
          print("Frame Value: RM", round(price_frame, 2))
          print("-" * 50)
          print("Estimated Value of Device: RM", round(value_price, 2))
          print("=" * 50)
        
      else:
        print("Invalid choice! Only enter '1' or '2'.")
        exit()
        
    else:
      print("Invalid device!")
      exit()
      
    total_price += value_price
    count += 1
  
print("_" * 85)
print("PAYMENT METHOD".center(85))
print("_" * 85)
payment_method = input("Enter your payment method(TNG/BANK): ").upper()

if payment_method == "TNG":
    phone_num = input("Enter your phone number(Type it without'-'): ")
  
elif payment_method == "BANK":
    bank = input("Enter preferred bank: ")
    account_number = input("Enter bank account number: ")
  
else:
    print("Invalid payment method")
    exit()

print("Email sent to the user's email.")
print("=" * 85)
print("RECEIPT".center(85))
print("=" * 85)
print("Name: ", name)
print("Email: ", email)
print("_" * 85)
print("Total Devices Processed: ", numdevice)
print("Total Payout Price: RM", round(total_price, 2))
print("_" * 85)
print("THANK YOU".center(80))
print("SERVICE WILL BE DONE IN 3 WORKING DAYS".center(85))
print("_" * 85)