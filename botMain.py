import time
import keyboard
import pyautogui


pyautogui.screenshot(region=(800, 859, 1000-700, 900-700)).save(r".\bin\testScreen.png")


def inputListen(x, listen):
    sleeptimer = 0.02
    reg = (800, 859, 1000-700, 900-700)
    conf = 0.86
    upArray = r'.\bin\UP.png'
    downArray = r'.\bin\DOWN.png'
    leftArray = r'.\bin\LEFT.png'
    rightArray = r'.\bin\RIGHT.png'

    if pyautogui.locateOnScreen(upArray,
                                region=reg,
                                confidence=conf) != None:
        while pyautogui.pixel(961,1016)[2] != (80, 200):
            time.sleep(sleeptimer)
        x += 1
        if x > len(steps):
            steps.append(1)
            listen = False

    if pyautogui.locateOnScreen(downArray,
                                region=reg,
                                confidence=conf) != None:
        while pyautogui.pixel(961, 1016)[2] != (80, 200):
            time.sleep(sleeptimer)
        x += 1
        if x > len(steps):
            steps.append(2)
            listen = False

    if pyautogui.locateOnScreen(leftArray,
                                region=reg,
                                confidence=conf) != None:
        while pyautogui.pixel(961, 1016)[2] != (80, 200):
            time.sleep(sleeptimer)
        x += 1
        if x > len(steps):
            steps.append(3)
            listen = False

    if pyautogui.locateOnScreen(rightArray,
                                region=reg,
                                confidence=conf) != None:
        while pyautogui.pixel(961, 1016)[2] != (80, 200):
            time.sleep(sleeptimer)
        x += 1
        if x > len(steps):
            steps.append(4)
            listen = False

    return x, listen

    # if pyautogui.locateOnScreen(r'.\bin\BLANK.png',
    #                             region=(708, 859, 1054 - 708, 1224 - 859),
    #                             confidence=0.75) != None:
    #     print("BLANK")


steps = []

x = 0
loops = 0
listen = True

while 1:
    if x < 3+loops:
        listen = True
    if listen:
        x, listen = inputListen(x, listen)
    else:
        time.sleep(1)
        for number in steps:
            if number == 1:
                keyboard.press_and_release('w')
                print("UP")
                time.sleep(0.2)
            if number == 2:
                keyboard.press_and_release('s')
                print("DOWN")
                time.sleep(0.2)
            if number == 3:
                keyboard.press_and_release('a')
                print("LEFT")
                time.sleep(0.2)
            if number == 4:
                keyboard.press_and_release('d')
                print("RIGHT")
                time.sleep(0.2)

        steps.clear()
        listen = True
        x = 0
        loops += 1
        print("##########################")
