#야구 게임
#세자리 중복없는 임의의수 만들자
#무한반복 ,사용자 입력을 받자
#strike, ball 판정하자 input()
#사용자입력한것 , strlike, ball 출력하자 print()
#임의의수랑 사용자 입력한게 같으면 hit, break  if
#random.sample(1,9+1),3) 샘플 3개 빼오기.
import random
r = random.randrange(1, 9+1)
r = str(r)
r1 = random.randrange(1, 9+1)
r1 = str(r1)
r2 = random.randrange(1, 9+1)
r2 = str(r2)

l = random.sample(range(1,9+1),3)
computer = ''.join(str(1) for i in l)

computer = "851"
while True:
  player = input("숫자 세자리 맞추기 :")
  strlike = 0
  ball =0
  #strlike, ball 판정하기
  for i in range(len(computer)):
      for j in range(len(player)):
          if computer[i] == player[j]:
              if i == j:
                  strlike += 1
              else:
                  ball +=1

  print("{}\tstrlike:{}\tball:{}".format(player,strlike,ball))
  if computer == player:
      print("HIT")
      break