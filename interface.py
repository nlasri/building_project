def interface_user(element):
    while True:
        try:
            num = int(input('Enter the size of the {}: '.format(element)))
            break
    
        except ValueError:
            print('Invalid Input. Try again.')
    
    return num

building_size = interface_user('building')