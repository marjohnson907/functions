# conversion calculator
# By: Mariel Johnson

# user input regarding the length to convert
# get the unit from the user
# convert the length to the correct unit
# output the answer to the user

user_number = float(input("What number would you like to convert? "))
user_unit = input("What unit is your number? ")

# to convert inches to mm, take inches multiplied by 25.4
# to convert mm to inches, take mm divide by 25.4

# user gives inches unit
conv_number = user_number * 25.4

print(conv_number)
print(user_unit)
