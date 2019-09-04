class Car:
    count = 0
    def __init__(self, type, speed):
        self.type = type
        self.speed = speed
        Car.count += 1 #count 만 쓰면 x

    @classmethod    #반드시 있어야함
    def get_count(cls): #꼭 이름이 cls 아니여도  o  
        return cls.count    #car.count 써도 o

    def move(self):
        print(self.type + "가" + str(self.speed)+ "속도로 움직입니다.")

    def speed_up(self, amount):
        self.speed += amount    #그냥 speed 쓰면 x

    def speed_down(self, amount):
        self.speed -= amount

print(Car.get_count())
c = Car("스포츠카", 200)
d = Car("마리오카트", 200)
c.speed_up(10)
c.move()
c.speed_down(10)
c.move()

d= Car("마리오카트",200)
d.speed_up(50)
d.move()
d.speed_down(150)
d.move()
print(Car.get_count())