import pyautogui
import time
text='Hello Pratik'


while True:
    time.sleep(2)  #for millisecond use 0.05        
    pyautogui.typewrite(text) 

    time.sleep(3)

    pyautogui.press('enter')
