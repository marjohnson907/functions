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
    #TODO address input from user without space
    values = user_input.rsplit(" ")
    number = values[0]
    
    if number.isdigit():
        number = float(number)
    else: 
        print("That is not a valid number.")
        valid_data = False
    unit = values[1]
    if unit != 'in' and unit != 'mm' and unit != 'ft':
        print("That is not a valid unit.")
        valid_data = False

    return number, unit

def print_results(user_number, user_unit, conv_number, conv_unit):
    user_number = user_number
    result = ("{:.2f} {} is equal to {:.2f} {}")
    print(result.format(user_number, user_unit, conv_number, conv_unit))
    

while True: # continue program until user exits
    while True: # check for valid data
        user_input = input("Number and unit to convert ")
        user_number, user_unit = user_parser(user_input)
        # check if there are invalid messages
        if valid_data:
            break
    # perform calculations
    if(user_unit == 'in'):
        conv_number = user_number * 25.4
        conv_unit = 'mm'
        #perform calculation in to mm
    elif(user_unit == 'mm'):
        conv_number = user_number / 25.4
        conv_unit = 'in'
    elif(user_unit == 'ft'):
        # perform ft to in
        conv_number = user_number * 12
        conv_unit = 'in'
    # Create a function that prints out the answer formatted to 2 decimal points
    # give the original value and unit and conv value and unit
    # 12.00 ft is equal to 144.00 in

    print_results(user_number, user_unit, conv_number,conv_unit)    
    
    
    
    
    
    
    
    
    
    
    


