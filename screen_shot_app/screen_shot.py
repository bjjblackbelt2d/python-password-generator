import pyautogui
import time

def screenshot():
    # time.sleep(5)
    name = time.time()
    name = '/home/seth/Development/Python/python-password-generator/screen_shot_app/screen_shots/{}.png'.format(name)
    img = pyautogui.screenshot()
    img.save(name)
    img.show()
    
screenshot()
    
   
