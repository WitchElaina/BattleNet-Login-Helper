import pyautogui
import pyperclip
import time
import settings
import os


def input_s(s, key):
    # Use copy and paste method to input string to avoid Chinese input source bugs:
    # for example:
    #   when input "xiaoheizi123" it may be "小黑子23" because input source thinks that we input "xiaoheizi" and select "1"
    pyperclip.copy(s)
    pyautogui.keyDown(key)
    pyautogui.press('a')
    pyautogui.press('v')
    pyautogui.keyUp(key)


def login(args):
    account = args[0]
    password = args[1]
    area = args[2]
    # judge OS mac/win
    if os.sep == '/':
        # mac
        key = 'command'
    else:
        # win
        key = 'ctrl'
    time.sleep(settings.WAIT_TIME)
    # input account and password
    input_s(account, key)
    pyautogui.press('tab')
    input_s(password, key)
    # check setting button
    pyautogui.hotkey('shift', 'tab')
    pyautogui.hotkey('shift', 'tab')
    pyautogui.press('space')
    # choose area
    pyautogui.press('tab', settings.AREA[area]+1)
    pyautogui.press('enter')
    # login
    time.sleep(1)
    pyautogui.press('tab', 4)
    pyautogui.press('enter')
