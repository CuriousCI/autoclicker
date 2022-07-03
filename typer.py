from pyautogui import press
import pyautogui

pyautogui.PAUSE = 0.05

if __name__ == '__main__':
    while True:
        press(['x', 'c', 'v', 'b'])