# 4.12
'''
def fakt():
    again = 'y'
    while again == 'y':
        n = input('Enter an integer to calculate the factorial for: ')
        try: 
            n = int(n)
            f_ = 1
            for el in range((n-1)):
                el += 2
                f_ *= el 
            print('Result: {} factorial is equal to {}'.format(n,f_))
            again = input('Do you want to calculate another factorial? (y/n): ')

        except ValueError:
            print('Integer entry error! Please try again.')
fakt()
'''
###########################################################
'''
# 4.13
def prime():
    print('\nCheck to see if your number is prime or composite.\n')
    again = 'y'
    while again == 'y':
        n = input('Enter a whole number to test: \n')
        try:
            n = int(n)
            for num in range((n-2)):
                num +=2
                if n % num == 0:
                    smell = num
                    print('Your number is composite because it is divisible by  {} .\n'.format(smell))
                    again = input('Would you like to check another number? (y/n): \n')
                    again = again.lower()
                    break
            else:
                print('The number  {}  is prime.\n'.format(n))
                again = input('Would you like to check another number? (y/n): ')
                again = again.lower()
                if again == 'y':
                    print()
        except ValueError:
            print('Integer input error! Please try again.\n')

prime()
    
'''

