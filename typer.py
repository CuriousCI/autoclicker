from pyautogui import press
import pyautogui

pyautogui.PAUSE = 0.02

if __name__ == '__main__':
    while True:
        press(['x', 'c', 'v', 'b'])