#p109
import random
# def rolling_dice():
#     n = random.randint(1,6) #1<=n<=6 랜덤수
#     print("6면 주사위 결과 : ", n)
# def rolling_dice(pip):
#     n = random.randint(1, pip)
#     print(pip, "면 주사위 결과", n)

# #같은 이름의 함수는 오버로딩이 없다 = 자료형이 없어서. (python은 java 처럼 함수 오버로딩 존재 X)
# rolling_dice(4)
# rolling_dice(6)
# rolling_dice(10)
# rolling_dice(9)
# rolling_dice(8)

# def rolling_dice(pip,repeat):
#     for r in range(1, repeat+1):
#         n = random.randint(1,pip)
#     print(pip, "면 주사위 결과",r, ":", n)

# rolling_dice(6,1)
# rolling_dice(6,2)
# rolling_dice(6,3)
# rolling_dice(6,4)
# rolling_dice(6,5)

# def star():
#      print("*****")
# star()
# star()
# star()

#p113
# print("♡")
# print("♡","♪")
# print("♡","♪","♣")
# print("♡","♪","♣","♠")
# print("♡","♪","♣","♠","★")

# def p(*args):
#     string =""
#     for a int args:
#       string += a
#     print(stirng.strip())

# print("♡")
# print("♡","♪")
# print("♡","♪","♣","♠")

#114
# def p (space, space_num, *args):
#     string = args[0]
#     for i in range(1, len(args)):
#         string += (space * space_num) + args[i]
#     print(string)

# p(",",3,"♡","♪")
# p("ha",2,"♡","♪","♣","♠")

def star2(s,*args):
    # for i in range(1, len(args)):
    #  print(s*args[i])
    for s in args:
        print(s*args)
 
star2("♬",3)
star2("♥",1,2,3)

#116
def fn(a,b,c,d,e):
    print(a,b,c,d,e)
fn(1 , 2 , 3 , 4 , 5)
fn(10 , 20 , 30 , 40 , 50)
fn(5 , 6 , 7 , 8 , 9)
fn(a=1 , b=2 , c=3 , d=4 , e=5)
fn(e=5, d=4 , c=3 , b=2 ,a=1)
#fn(1, , 2, c=3, e=5, d=4) error

#p.118
# def star3(mark, repeat, space,repeat_space,line ):
#         for _ int range(line):
#             string t = (mark*repeat) +(space *repeat_space) + (mark * repeat)
#             print(string)

#         star3("*",3,"_",2,3)

#p.119
def hello(name="무명",msg="안녕하세요"):
        print(name+"님"+msg+"!")
hello("김철수","오랜만이에요")
hello()

#p.120
def hello1(name, msg="안녕하세요"):
        print(name + "님" + msg + "!")
hello1("김철수","오랜만")
hello1("이영희")

def fn2(a, b=[]):
        b.append(a)
        print(b)
fn2(3)
fn2(5)
fn2(10)
fn2(7,[1])

#p123

def gugudan(dan=2):
 for i in range(1,10):    # 1부터 9까지 곱할 숫자
    print(str(dan),"X",str(i),dan*i)
gugudan(3)
gugudan(2)
gugudan()
#p.125  
def sum(*numbers):
        sum_value=0
        for numbers in numbers:
                sum_value = sum_value +numbers
                return sum_value
        result = sum(1,3)
        print("1+3",result)
        print("1+3+5+7",sum(1,3,5,7))

# def min(*numbers):
#         min_value = numbers[0]
#         for numbers in numbers:
#          if min_value < numbers:
#  return min_value
#  result = min(1,3)  
#  print("min(1+3+5-2)",result)              
#  print("min(1+3+5-2)",min(1,3,5,7))

# def max(*numbers):
#          max_value = numbers[0]
#         for numbers in numbers:
#           if max_value < numbers:
#                 max_value = numbers
#         return max_value
  
# print("multi_num(17,1,200 =",multi_num(17,1,200))
# print("multi_num(3,1,100 =",multi_num(3,1,100))
 
# def min_max(*args):
#         min_value =args[0]
#         min_value = args[0]
        
#         for a in args:
#                 if min_value =a:
#                 min_value =a 
#                 if max_value <a:
#                         max_value=a
#         return min,max
#         min,max = min_max(53,-3,23,89,-21)
#         print("최솟값:",min,"최댓값:",max)