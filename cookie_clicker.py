import win32api, win32con
import time
import keyboard

def click():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(0.01)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
    
# press p to start the clicker
keyboard.wait("p")
time.sleep(2)
while True:
    click()
    # press p to stop the clicker
    if keyboard.is_pressed("p"):
        break