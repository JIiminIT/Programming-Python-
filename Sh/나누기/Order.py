from drink import Drink
from bubbleTea import BubbleTea
class Order :
  _drinks = [Coffee("아메리카노", 1800), BubbleTea("민트초코버블티", 3300)]
  def _init_ (self) :
    self.order_menu = []

  def show_menu (self) :
    print("0 : 아메리카노 1800원 | 1 : 민트초코버블티 3300원")

  def order_drink (self) :
    #반복
    while True:
    #show_menu
     self.show_menu()
    #주문, 음료선택, 음료 옵션 선택 _ 반복
     order = input("무엇을 선택하시겠습니까? ")
     if order == "":
         break
     drink = Order._drinks[int(order)]
     drink.order()

    self.order_menu.append(drink)
    #주문 음료 내용 출력
    for d in self.order_menu :
      print(d)
    #합계 금액
    self.sum_price()
    print("총 주문 금액 : " + str(self.sum_price()) + "원")

  def sum_price(self):
    sum = 0
    for d in self.order_menu :
      sum += d.price
    return sum
