f =open("file.txt","w")

try:
    f.write("Hello world")
    f.write(100)
except TypeError:
    print("타입 예외 발생 (100을 쓸 수 없음)")
finally:
    print("예외 여부와 상관없이 무조건 실행")
    f.close()