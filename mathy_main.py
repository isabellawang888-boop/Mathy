def mathy():
    import time

    time.sleep(1)
    print('Hello! Welcome to the mathy daily mission!')
    time.sleep(1)
    print('choose a system and an operation to start your daily mission.\n')
    time.sleep(1)
    choice_system = input('Choose: 1.quality\n 2.quantity\n:')
    time.sleep(1)
    choice_operation = input('Choose: 1.addition\n 2.subtraction\n 3.multiplication\n:')
    time.sleep(1)

    if choice_system == '1':
        if choice_operation == '1':
            print('You have chosen the quality system and addition operation.')
            from quality.addition import quality_addition
            quality_addition()
        elif choice_operation == '2':
            print('You have chosen the quality system and subtraction operation.')
            from quality.subtraction import quality_subtraction
            quality_subtraction()
        elif choice_operation == '3':
            print('You have chosen the quality system and multiplication operation.')
            from quality.multiplication import quality_multiplication
            quality_multiplication()
        else:
            print('Invalid choice. Please choose a valid operation.')
    
    elif choice_system == '2':
        if choice_operation == '1':
            print('You have chosen the quantity system and addition operation.')
            from quantity.addition import quantity_addition
            quantity_addition()
        elif choice_operation == '2':
            print('You have chosen the quantity system and subtraction operation.')
            from quantity.subtraction import quantity_subtraction
            quantity_subtraction()
        elif choice_operation == '3':
            print('You have chosen the quantity system and multiplication operation.')
            from quantity.multiplication import quantity_multiplication
            quantity_multiplication()
        else:
            print('Invalid choice. Please choose a valid operation.')

    
    time.sleep(1)
    print('Thank you for playing! See you tomorrow!')


if __name__ == '__main__':
    mathy()
