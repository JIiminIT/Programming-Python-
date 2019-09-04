
print("주문은 뭘로 하시겠습니까?")
print("<1>카푸치노 <2>카페라떼 <3>아메리카노 <4> 그만할래요")
while True:
    x = int(input("주문번호를 입력하시오 :"))
    if x == 4:
        print("주문을 그만합니다.")
        break
    elif x==1:
        print("아메리카노 나왔습니다.")
    elif x==2:
        print("카페라떼 나왔습니다.")
    elif x==3:
        print("카페라떼 나왔습니다.")
            
  