f =open("file.txt", "r", encoding=="utf8") #r: read test

text = f.read()
print(text)

f.close()

#한줄씩 읽어오자
f =open("file.txt", "r", encoding=="utf8") #r: read test

text0 = f.readline() #\n 까지 읽기
print(text0)

text1 = f.readline()
print(text1)

text2 = f.readline()
print(text2)

f.close()