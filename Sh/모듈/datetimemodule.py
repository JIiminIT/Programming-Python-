from  datetime import datetime

print('햔재 날짜 시각 객체 얻기')
today = datetime.now()
print('datetime.now() :', today)

print('연,월,일 :' ,today.year, today.month, today.day) #month 1은 1월 다른 언어는 0부터 시작함
print('시,분,초 :', today.hour, today.minute, today.second)
print('요일 :', today.weekday()) #0은 원요일. 1은 화요일

print('특정 날짜 시각 객체 만들기')
day =datetime(2019,1,1,0,0,0)

print('day =datetime(2018,1,1,0,0,0) :', day)

print('2019년부터 지나온 시간 구하기')
print('today - day :', today - day)

HBD = datetime(2002,11,27,4,27,0)
print('내가 태어날 날은 무슨요일?')
print(HBD.weekday())

#나는 며칠 살았을까
print('2002년부터 지나온 시간 구하기')
print('day =datetime(2002,11,27,4,27,0) :', HBD)
print('today - HBD :', today - HBD)

#크리스마스 몇일 남았을까
CHBD = datetime(2019,12,25,0,0,0)
print(today - CHBD)

