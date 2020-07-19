year = int(input('Enter a 4 digit year : '))
leap = lambda x : print(x,'is a leap year.') if (x % 4 == 0 and x % 100 != 0) or x % 400 == 0\
else print(x,'is not a leap year.')
leap(year)
