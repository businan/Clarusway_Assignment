print("""
###################################
Please give your answers such as 
If your answer is 'Yes' hit the any key on keyboard than click Enter 
If your answer is 'No' just hit Enter on keyboard
###################################
""")
age = bool(input('Are you a cigarette addict older than 75 years old? '))
chronic = bool(input('Do you have a severe chronic disease? '))
immune = bool(input('Is your immune system too weak? '))
if age and chronic and immune :
    print('\nYou are in risky group')
else:
    print('\nYou are not in risky group')