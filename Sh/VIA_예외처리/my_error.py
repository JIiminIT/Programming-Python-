class Error(Exception):
    def __init__(self, massage = "홀수 ㄴ"):
        self.massage = massage

    def __str__(self):
        return self.massage

n = 11
try:
    if n%2 != 0:
        raise OddError #에러 발생
    else:
        print("짝수에요. 짝짝짝")
except OddError as e:   #에러처리
    print(e)