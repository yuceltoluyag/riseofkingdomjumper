import pyautogui as auto
from python_imagesearch.imagesearch import imagesearch as search
import time,random,sys
from colorama import init
init()
from colorama import Fore, Back, Style
# print(Fore.RED + 'some red text')
# print(Back.GREEN + 'and with a green background')
# print(Style.DIM + 'and in dim text')
# print(Style.RESET_ALL)
# print('back to normal now')
auto.FAILSAFE = False


def onscreen(path, confidence=0.9):
    return search(path, confidence)[0] != -1


def search_to(path):
    pos = search(path)
    if onscreen(path):
        auto.moveTo(pos)
        # print(path + " found")
        return pos
#   else:
    #   print(path + " not found")

def click_key(key, delay=.1):
    auto.keyDown(key)
    time.sleep(delay)
    auto.keyUp(key)

def click_left(delay=.1):
    auto.mouseDown()
    time.sleep(delay)
    auto.mouseUp()


def click_right(delay=.1):
    auto.mouseDown(button='right')
    time.sleep(delay)
    auto.mouseUp(button='right')


def click_to(path, delay=.1):
    if onscreen(path):
        auto.moveTo(search(path))
        click_left(delay)
        # print(path + " clicked")


def main():
    buldurcan()


# Start main process
def buldurcan():
    if onscreen("./img/novisit1.png"):
        click_to("./img/novisit1.png")
    while not onscreen("./img/novisit1.png"):
        auto.keyDown('down')
        print(Fore.RED + 'Zoom Out')
    auto.keyUp('down')
    time.sleep(3)
    print(Fore.GREEN + 'Hedef Bulundu')
    click_to("./img/novisit1.png")
    hediyetopla()
    time.sleep(3)

def hediyetopla():
    time.sleep(5)
    if onscreen("./img/giftme.png"):
      print(Fore.RED + "Hediye Toplanıyor.")
      time.sleep(1)
      click_to("./img/giftme.png")
      time.sleep(1)
      click_left()
      time.sleep(2)
      click_to("./img/welcome.png",2)
      click_to("./img/awesome.png",2)
      time.sleep(1)
      main()
    while not onscreen("./img/giftme.png"):
        print(Fore.LIGHTWHITE_EX + "Gece Modu")
        click_to("./img/giftmenight.png")
        click_left()
        time.sleep(3)
        main()
        print(Fore.LIGHTCYAN_EX + "İşlem Başa Alındı")

if __name__ == '__main__':
    main()

# kacsaniye = 1
# kac_tik = 3
# tik_arasi = 1
# resimbul = pyautogui.locateOnScreen('img/novisit.png', confidence=0.9)
# print(resimbul)
# pyautogui.moveTo(resimbul, duration=kacsaniye)
# pyautogui.click(resimbul, clicks=kac_tik, interval=tik_arasi, button='left')
# hediyebul = pyautogui.locateOnScreen('img/giftme.png',confidence=0.9)
# pyautogui.FAILSAFE = True
# pyautogui.moveTo(hediyebul, duration=2)
# print(hediyebul)
# pyautogui.click(hediyebul, clicks=kac_tik, interval=tik_arasi, button='left')

# # im1=pyautogui.screenshot()
# # im2=pyautogui.screenshot("newone.png")
# # Image.open("newone.png").convert("RGB").save("newone.png")
# # print(pyautogui.size())
