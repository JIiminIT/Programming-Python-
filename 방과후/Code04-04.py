a =100
result = 0
i = 0

for i in range(1,5):
    result = a << i
    print("%d << %d = %d" %(a,i,result))

for i in range(1,5):
    result = a >> i
    print("%d >> %d = %d" % (a,i,result))

input(int('정수를 입렫하시오'))

#다른 문제

# number = int(input("정수를 입력하시오:"))
#
# sum =0
# sum = sum + number % 10
# number =number //10
# sym = sum + number % 10
# number = number //10
# sum = sum + number // 10
