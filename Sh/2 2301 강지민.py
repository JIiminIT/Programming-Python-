num = input("숫자를 입력하세요. : ")
list = []
sum = 0

for i in num:
    list += i
for j in range(0, len(num)):
    sum += int(list[j])
print(sum)