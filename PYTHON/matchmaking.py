num = int(input("Enter any number: "))

match num:
    case 18:
        print('Now you are a teenage.')
    case 25:
        print('Now you are ready to marriage.')
    case 60:
        print('This is your Retirement')
    case _:
        if num > 60:
            print('not possible')
        if num < 18:
            print('You are a child')
