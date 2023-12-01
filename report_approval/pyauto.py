import pyautogui
import time
import keyboard

from functions import *


queue = find_image_center(queue_image, 0.9)
while queue:
  rejected  = False
  view_report()
  rejected = screen_report()
  if rejected:
    reject_report(rejected)
  else:
    approve_report()
  queue = check_queue()






pyautogui.screenshot(region=(270, 370, 34, 55)).save(r'images/test.png')

location=find_image_center(r'images/test.png')
pyautogui.moveTo(location[0], location[1], duration=0.4)



view_report('/Users/schuyler.smith@nutrien.com/Desktop/pyAutoTest/images/df_report.png')