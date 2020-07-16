for i in range(1,101):
    if i % 15 == 0 :
        print(i, 'is FizzBuzz')
    elif i % 3 == 0 :
        print(i, 'is Fizz')
    elif i % 5 == 0 :
        print(i, 'is Buzz')
    else:
        print(i, 'is unchanged')
