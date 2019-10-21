#main.py

from order import Order
from file_manager import FileManager

#히스토리가 있으면 내역 찾아주기

file_manager = FileManager("history.bin")

#보여주기
history = []

try:
    history = file_manager.load()
    sum = 0
    for d in history:
        print(h)
        sum += h.price
    print('내가 그동안 아마스빈에 퍼부은 돈' + str(sum)+ '원')
except FileNotFoundError:
    print("내역이 없습니다.")

print("------------------------------------------------------------------------------")

o = Order()
o.order_drink()

#히스토리 저장하기
file_manager.save(o.order_menu)