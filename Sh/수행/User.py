# 현재 소지하고 있는 잔액으로 대중교통을 n번 이용이 가능한지 알려주는 기능입니다.
class User():
  def set_age(self): 
    #연령대 요금을 판별합니다.
    self.age= int(input("나이를 입력해주세요. :"))
    if self.age <=5: #어린이
      self.agemoney = 450
    elif self.age <=19 : #청소년
      self.agemoney =  720
    elif self.age < 20: #성인
      self.agemoney = 1250

  #현재 소지하고 있는 잔액을 물어봅니다.
  def set_money(self):
    self.money= int(input("잔액을 입력해주세요. :"))

  #시간에 따라 할인요금이 적용되기 때문에 탑승 시간을 물어봅니다.
  def set_time(self):
    self.time= int(input("오전 6시 30전에 이용하십니까? (1.네 | 2. 아니요.): "))
    if self.time == 1:
      self.timem = int(self.agemoney * 0.2) # 기본요금에 %20이 적용됩니다. 
    elif self.time == 2:
      self.timem = int(self.agemoney)
    
  #왕복이라면 나누기 2를 하고 아니라면 편도라면 잔액 나누기 요금만 해줍니다.
  def set_movenum(self):
    self.movenum = int(input("이용하시는 번호를 입력해주세요. ( 1.한번  / 2. 왕복)  :"))

    #잔액 나누기 연령요금 나누기 값(time 선택에 따라 할인율이 적용됩니다.)

    if self.movenum == 1 and self.time == 1 :
      result = int(self.money // self.agemoney - self.timem)
      print("이용가능 횟수는",result,"번 입니다.")

    elif self.movenum ==2 and self.time == 1:
      result = int(self.money / self.agemoney // 2 -self.timem)
      print("이용가능 횟수는",result,"번 입니다.")

    elif self.movenum ==1 and self.time ==2:
      result = int(self.money // self.agemoney)
      print("이용가능 횟수는",result,"번 입니다.")

    elif self.movenum ==2  and self.time ==2:
      result = int(self.money / self.agemoney // 2)
      print("이용가능 횟수는",result,"번 입니다.")


s = User()
#무한루프
while True :
  s.set_age()
  s.set_money()
  s.set_time()
  s.set_movenum()
  #1을 입력하면 종료가 되고 아니면 계속 돌아갑니다.
  stop = int(input("그만 하시겠습니까? (1.네 | n. 아니요.): "))
  if stop == 1 :
    print("프로그램을 종료합니다.")
    break