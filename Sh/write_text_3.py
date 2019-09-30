fi = open("test.jpg", "w", encoding= "utf8")

fi.write("아이스 아메리카노\t:2800원\t100%\t50%\t코코")
fi.write("오레오쉐이크\t:3800원\t100%\t50%\t타피오카")
fi.write("딸기코코넛\t:4800원\t100%\t50%\t알로에")

fi.close()

fi = open("test.ama" , "r", encoding="utf8")
sum = 0
while True:
    data = fi.read()
    if not data:
        break
    l = data.split("\t") #화이트스페이스(띄어쓰기, \t,\n 등) 분리
    print(l)
    #저장하고 불러오고 합계구하기
    sum += int(l[l]+"원")
fi.close()
print("주문한 총금액:" +str(sum)+ "원")
