import pyautogui as pag
import time

if __name__ == '__main__':

    #크롬 이미지 인식하기
    data = pag.locateAllOnScreen("크롬아이콘.PNG")
    print(data)

    #가운데 좌표 찾자
    center  = (data.left + (data.width 2), data.top(data.height/2))

    #마우스 이동하자
    pag.moveTo(center,duration=2)

    #더블 클릭하자
    pag.doubleClick(2)