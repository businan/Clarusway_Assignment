number = input('Enter a number that you you want to check : ')
arm_num = 0
if number.isdigit():
    for i in number:
        arm_num += int(i)**len(number)
    if arm_num == int(number):
        print(number,'is an Armstrong number')
    else:
        print(number,'is not an Armstrong number')

elif '.' in number:
    print('Please enter an integer number')
elif number:
    for i in number:
        if i.isalpha():
            print('Do not use any entries other than numeric values')
            break
        else:
            print('Please enter a positive number')
            break





    



#print('Do not use any entries other than numeric values')

