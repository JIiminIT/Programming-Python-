for dan in range(2, 9+1):
    for i in range(1, 9+1): 
        if i%2 == 1:
            continue
        print(dan, "X",i, "=", dan*i)
    print("=====================")