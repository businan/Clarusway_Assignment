lst = [1,1]
start = 2
last = int(input('How many fibanacci numbers do you want to see?  '))
for i in range(last):
    if start == last:
        break
    start += 1
    lst.append((lst[i+1]+lst[i]))
print(lst)
