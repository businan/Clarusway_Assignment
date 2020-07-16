def fizzbuzz(x, y):
    for i in range(x, y):
        if i % 15 == 0 :
            print(i, 'is FizzBuzz')
        elif i % 3 == 0 :
            print(i, 'is Fizz')
        elif i % 5 == 0 :
            print(i, 'is Buzz')
        else:
            print(i, 'is unchanged')
start = int(input("Enter number that you want to start searching in FizzBuzz : "))
stop = int(input("Enter number that you want to finish searching in FizzBuzz : "))
fizzbuzz(start,stop)
