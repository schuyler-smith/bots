import pyautogui
import time
import keyboard

from images import *

def find_image_center(image_path, confidence=None):
  try:
    if confidence:
      location = pyautogui.locateOnScreen(image_path, confidence=confidence)
    else:
      location = pyautogui.locateOnScreen(image_path)
    return pyautogui.center(location)
  except pyautogui.ImageNotFoundException:
    return None

def view_report(sample_group=None):
  report = find_image_center(bagID_image, 0.9)
  # click onto page to activate js
  pyautogui.click(report[0], report[1])
  time.sleep(1)
  pyautogui.click(report[0], report[1])
  if sample_group:
    scroll = 1
    report = find_image_center(sample_group, 0.9)
    if not report:
      while scroll <= 10 and not report:
        pyautogui.hotkey('pagedown')
        report = find_image_center(sample_group, 0.9)
        scroll += 1
    report = (report[0]+30, report[1])
  else:
    report = (report[0], report[1]+40)
  # click first item below bagID
  pyautogui.moveTo(report[0], report[1], duration=0.3)
  pyautogui.click(report[0], report[1])
  # wait for report to load
  time.sleep(2.5)

def approve_report():
  # click approve
  approve  = find_image_center(approve_image, 0.95)
  pyautogui.moveTo(approve[0], approve[1], duration=0.4)
  pyautogui.click(approve[0], approve[1])
  time.sleep(1)
  # click yes
  yes  = find_image_center(yes_image, 0.9)
  pyautogui.moveTo(yes[0], yes[1], duration=0.4)
  pyautogui.click(yes[0], yes[1])

def reject_report(message):
  reject  = find_image_center(reject_image, 0.9)
  pyautogui.moveTo(reject[0]+60, reject[1], duration=0.3)
  pyautogui.click(reject[0]+60, reject[1])
  pyautogui.moveTo(reject[0], reject[1], duration=0.3)
  pyautogui.click(reject[0], reject[1])
  time.sleep(0.3)
  reason  = find_image_center(reason_image, 0.9)
  pyautogui.click(reason[0], reason[1])
  pyautogui.moveTo(reason[0], reason[1]+40, duration=0.3)
  pyautogui.click(reason[0], reason[1]+20)
  pyautogui.typewrite(message, interval=0.001)
  yes  = find_image_center(yes_rej_image, 0.9)
  pyautogui.moveTo(yes[0], yes[1], duration=0.2)
  pyautogui.click(yes[0], yes[1])

def check_queue():
  # wait for API to send response and reload homepage
  time.sleep(2)
  queue = find_image_center(queue_image, 0.9)
  empty = find_image_center(empty_image, 0.8)
  while not queue and not empty:
    time.sleep(1)
    queue = find_image_center(queue_image, 0.9)
    empty = find_image_center(empty_image, 0.8)
  return(queue)

def screen_report():
  message   = []
  # scan for bad
  biomass   = find_image_center(biomass_image)
  bacteria  = find_image_center(bacteria_image)
  fungi     = find_image_center(fungi_image)
  if all([biomass, bacteria, fungi]):
    message.append("failed DNA extraction")
  else:
    if biomass:
      pyautogui.moveTo(biomass[0], biomass[1], duration=0.3)
      message.append("biomass measurement failed\n")
    if bacteria:
      pyautogui.moveTo(bacteria[0], bacteria[1], duration=0.3)
      message.append("bacteria measurement failed\n")
    if fungi:
      pyautogui.moveTo(fungi[0], fungi[1], duration=0.3)
      message.append("fungi measurement failed\n")
    ammonifiers = find_image_center(ammonifiers_image)
    # brady       = find_image_center(brady_image)
    denitrifier = find_image_center(denitrifier_image)
    n2o         = find_image_center(n2o_image)
    nconserv    = find_image_center(nconserv_image)
    nfixers     = find_image_center(nfixers_image)
    nitri_bal   = find_image_center(nitri_bal_image)
    nitrifiers  = find_image_center(nitrifiers_image)
    mineral     = find_image_center(mineral_image)
    mycorrihza  = find_image_center(mycorrihza_image)
    solubilizer = find_image_center(solubilizer_na)
    if ammonifiers:
      pyautogui.moveTo(ammonifiers[0], ammonifiers[1], duration=0.3)
      message.append("ammonifiers measurement failed\n")
    # if brady:
    #   message.append("brady measurement failed\n")
    if denitrifier:
      pyautogui.moveTo(denitrifier[0], denitrifier[1], duration=0.3)
      message.append("denitrifier measurement failed\n")
    if n2o:
      pyautogui.moveTo(n2o[0], n2o[1], duration=0.3)
      message.append("n2o measurement failed\n")
    if nconserv:
      pyautogui.moveTo(nconserv[0], nconserv[1], duration=0.3)
      message.append("nconserv measurement failed\n")
    if nfixers:
      pyautogui.moveTo(nfixers[0], nfixers[1], duration=0.3)
      message.append("nfixers measurement failed\n")
    if nitri_bal:
      pyautogui.moveTo(nitri_bal[0], nitri_bal[1], duration=0.3)
      message.append("nitri_bal measurement failed\n")
    if nitrifiers:
      pyautogui.moveTo(nitrifiers[0], nitrifiers[1], duration=0.3)
      message.append("nitrifiers measurement failed\n")
    if mineral:
      pyautogui.moveTo(mineral[0], mineral[1], duration=0.3)
      message.append("mineral measurement failed\n")
    if mycorrihza:
      pyautogui.moveTo(mycorrihza[0], mycorrihza[1], duration=0.3)
      message.append("mycorrihza measurement failed\n")
    if solubilizer:
      pyautogui.moveTo(solubilizer[0], solubilizer[1], duration=0.3)
      message.append("solubilizer measurement failed\n")
  return("".join(message))



