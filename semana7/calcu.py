def menu(Current):
    print(f'Number {Current}')
    print('1.  Addition')
    print('2.  Multiply')
    print('3.  Subtract')
    print('4.  Division')
    print('5. Reset to 0')
    print('6. Exit')

def addition(Current,number):
    return Current+number
def Multiply(Current,number):
    return Current*number
def Subtract(Current,number):
    return Current-number
def Division(Current,number):
    if number==0:
        raise ZeroDivisionError('You can never do that!')
    return Current/number
    

def gettingnumber():
    while True:
        try:
            return float(input('Enter the number for the operation'))
        except ValueError as error:
            print(f'The number wasn´t right: {error}')
        except Exception as error:
            print(f'The error is:   {error}')
def main():
    Current=0.0
    while True:
        menu(Current)
        select=input('Choice an option from 1 to 6:')
        if select=='6':
            print('Shutting off, cya later!')
            break
        elif select=='5':
            Current=0.0
            print('Reset the result to 0')
            continue
        elif select not in ['1','2','3','4']:
            print('The option selected is not aviable')
            continue
        number=gettingnumber()
    
        try:    
            if select=='1':
                Current=addition(Current,number)
            elif select=='2':
                Current=Multiply(Current,number)
            elif select=='3':
                Current=Subtract(Current,number)
            elif select=='4':
                Current=Division(Current,number)
        except ZeroDivisionError as error:
            print(f'Have divided by 0 omg!-{error}')
        except ValueError as error:
            print(f'Don´t worry! let´s try again {error}')

    print(f'The result is {Current}')
if __name__=="__main__":
    main()