# conversion calculator
# By: Mariel Johnson

# user input regarding the length to convert
# get the unit from the user
# convert the length to the correct unit
# output the answer to the user
valid_data = True

def user_parser(user_input):
    global valid_data
    valid_data = True
    values = user_input.rsplit(" ")
    number = values[0]
    
    if number.isdigit():
        number = float(number)
    else: 
        print("That is not a valid number.")
        valid_data = False
    unit = values[1]
    if unit != 'in' and unit != 'mm':
        print("That is not a valid unit.")
        valid_data = False

    return number, unit

while True: # continue program until user exits
    while True: # check for valid data
        user_input = input("Number and unit to convert ")
        user_number, user_unit = user_parser(user_input)
        # check if there are invalid messages
        if valid_data:
            print('User number', user_number)
            print('User unit', user_unit)
            break
    # perform calculations
    if(user_unit == 'in'):
        conv_number = user_number * 25.4
        conv_unit = 'mm'
        #perform calculation in to mm
    elif(user_unit == 'mm'):
        conv_number = user_number / 25.4
        conv_unit = 'in'
    print(conv_number, conv_unit)    
    
    
    
    
    
    
    
    
    
    
    


