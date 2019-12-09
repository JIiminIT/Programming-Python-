import pyautogui as pag
import time

if __name__  == '__main__':

    #메모장 프로그램 실행하자
    pag.moveTo(10, 1065, 1)
    pag.click()
    pag.press("hangul")
    pag.typewrite("apahwkd")
    # pag.press("enter")
    pag.press("enter")


    #Hello world 치자
    time.sleep(2)
    pag.press("enter")
    pag.typewrite("Hello world")

    #두번 내리자
    pag.press("enter")
    pag.press("enter")


    #반갑구나 세상아 치자
    pag.press("hangul")
    pag.typewrite("qksrkqrnsk tptkddk")
    time.sleep(2)

    #저장하자
    pag.hotkey('ctrl','s')
    time.sleep(1)

    #파일이름 : 파이썬월드
    pag.press("hangul")
    pag.typewrite("C:\\Users\\LG\\Downloads")
    pag.typewrite("vkdlTjsdnjfem")

