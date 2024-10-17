
print ("Welcome to the tip calculator!")
bill = float(input("What was the total bill ?"))
tip = float(input("How much would you like to give? 10,12, or 15?"))
person = int(input("How many people to split the bill ?"))
per_person = round(((bill + tip) / person),2)
print(f'Each person should pay $ :{per_person}')
