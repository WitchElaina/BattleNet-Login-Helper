import pyautogui
import pyperclip
import time
import settings


def login(args):
    account = args[0]
    password = args[1]
    area = args[2]
    time.sleep(settings.WAIT_TIME)
    # input account and password
    pyperclip.copy(account)
    pyautogui.hotkey('ctrl', 'v')
    pyautogui.press('tab')
    pyperclip.copy(password)
    pyautogui.hotkey('ctrl', 'v')
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
