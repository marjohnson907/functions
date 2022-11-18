# conversion calculator
# By: Mariel Johnson

# user input regarding the length to convert
# get the unit from the user
# convert the length to the correct unit
# output the answer to the user

while True: 
    while True:
        user_number = input("What number would you like to convert? ")
        if user_number.isdigit():
            user_number = float(user_number)
            break
        else:
            print('Please use a number.')
            
    user_unit = input("What unit is your number? ")

        # to convert inches to mm, take inches multiplied by 25.4
        # to convert mm to inches, take mm divide by 25.4

        # user gives inches unit

    if(user_unit == 'in'):
        conv_number = user_number * 25.4
        conv_unit = 'mm'
        break
        #perform calculation in to mm
    elif(user_unit == 'mm'):
        conv_number = user_number / 25.4
        conv_unit = 'in'
        break
        #perform mm to in calc
    else:
        print('That is not a valid unit.')

print(conv_number, conv_unit)

