sudoku = [
    [0, 0, 0, 0, 6, 4, 0, 0, 0],
    [7, 0, 0, 0, 0, 0, 3, 9, 0],
    [8, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 5, 0, 2, 0, 6, 0],
    [0, 8, 0, 4, 0, 0, 0, 0, 0],
    [3, 5, 0, 6, 0, 0, 0, 7, 0],
    [0, 0, 2, 0, 0, 0, 1, 0, 3],
    [0, 0, 1, 0, 5, 9, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 7, 0, 0]
]
count = 1
num = 0
for i in range(len(sudoku)):
    if i%3==0:
        print('\n---------------------',end='')
    for j in sudoku[i]:
        if num%9==0:
            print()
        (lambda j : print(str(j)+' |' , end=' ') if (count==3 or count==6) else print(str(j),end=' ')) (j)
        count += 1
        num += 1
    count = 1
print('\n---------------------',end='')
