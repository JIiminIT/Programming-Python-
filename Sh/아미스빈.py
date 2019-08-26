class Drink :
  _cups = ["레귤러", "점보"]
  _ice = ["0%", "50%", "100%", "150%"] 
  _sugar = ["0%", "50%", "100%", "150%"]

  def _init_ (self, name, price) :
    self.name = name
    self.price = price
    self.cup = 0 # 0 레귤러 1 점보
    self.ice = 2 # 0 0% 1 50% 2 100% 3 150%
    self.sugar = 2 # 0 0% 1 50% 2 100% 3 150%

  def set_cup (self) :
    self.cup = input("컵사이즈를 선택하세요 (0:레귤러 1:점보) : ")
    if self.cup == "":
      self.cup = 0
    else :
      self.cup = int(self.cup)
      if self.cup == 1 :
        self.price += 500

  
  def set_ice (self) :
    self.ice = input("얼음 양을 선택하세요 (0:0% 1:50% 2:100% 3:150%) : ")
    if self.ice == "":
      self.ice = 2
    else :
      self.ice = int(self.ice)
  
  def set_sugar (self) :
    self.sugar = input("당도를 선택하세요 (0:0% 1:50% 2:100% 3:150%) : ")
    if self.sugar == "":
      self.sugar = 2
    else :
      self.sugar = int(self.sugar)

  def _str_ (self) : 
    return "주문내역 : 제품명 " + self.name + ", 가격 " + str(self.price) + ", 컵사이즈 " + Drink._cups[self.cup] + ", 얼음량 " + Drink._ice[self.ice] + ",당도 " + Drink._sugar[self.sugar]

  def order(self) :
    self.set_cup()
    self.set_ice()
    self.set_sugar()

class Coffee(Drink) :
  pass

class BubbleTea(Drink) :
  _pearl = ["타피오카", "코코", "젤리", "알로에"]

  def _init_ (self, name, price) : 
    super().__init__(name, price)
    self.pearl = 0 # 0 타피오카 1 코코 2 젤리 3 알로에

  def set_pearl (self) :
    self.pearl = input("펄을 선택하세요 (0:타피오카 1:코코 2:젤리 3:알로에) : ")
    if self.pearl == "" :
      self.pearl = 0
    else :
      self.pearl = int(self.pearl)

  def _str_ (self) :
    return super().__str__() + ", 펄 " + self._pearl[self.pearl]

    def order(self) :
      # self.set_cup()
      # self.set_ice()
      # self.set_sugar()
      super().order()
      self.set_pearl()

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

o = Order()
o.order_drink()

아메리카노 = Drink("아메리카노", 1800)
아메리카노.set_cup()
아메리카노.set_ice()
아메리카노.set_sugar()
print(아메리카노)

민트초코버블티 = BubbleTea("민트초코버블티", 3300)
민트초코버블티.set_cup()
민트초코버블티.set_ice()
민트초코버블티.set_sugar()
민트초코버블티.set_pearl()
print(민트초코버블티)