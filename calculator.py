print("Welcome to this tip calculator.")
bill = int(input("What was the total bill? "))
tip = float(input("How much tip would you like to give? 10, 12, or 15? "))
no_of_pple_t0_split_with = int(input("How many people to split the bill? "))
Amount_to_pay = ((tip/100) * bill + bill)/no_of_pple_t0_split_with
print("Each person should pay: {: .2f}" .format(Amount_to_pay))