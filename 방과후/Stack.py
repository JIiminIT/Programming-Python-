parking = []
top,carName,outCar = 0, "A",""
select = 9

##main 코드 부분

while (select !=3):
    select = int(input("<1>자동차 넣기 <2> 자동차 빼기 <3> 끝:"))

    if(select == 1):
         if(top >=5):
            print('주차장이 꽉 차서 못 들어감')
         else:
             parking.append(carName)
             print("%자동차 들어감. 주차장 상태 ==>%s" %(parking[top], parking))
             top += 1
             carName = chr(ord(carName)+1)