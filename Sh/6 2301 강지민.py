
for i in range(1, 99+1, 1):
    i = str(i)
    if len(i) ==2:
        if i[0] == '3' or i[0] == '6' or i[0] == '9':
            print("짝")
        elif i[1] == '3' or i[1] == '6' or i[1] =='9':
            print("짝")
        else:
            print(i)
    else:
        if i[0] == '3' or i[0] == '6' or i[0] =='9':
            print("짝")
        else:
            print(i)