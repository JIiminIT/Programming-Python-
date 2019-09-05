def gugudan(n):
    print(n,"단을 출력합니다.")
    for i in range(1,0+1):
        print(n,"+",1,"-",n*1)

if __name__ == '__mian__': #자기 모듈 실행하면 실행되고 import 실행 x
    gugudan(3)