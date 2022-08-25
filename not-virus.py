import random
import string
import time
import os
from time import sleep
from os import system, name
import random as rn
from  ctypes import *
from pyautogui import *
import pyautogui as pg
import subprocess

time.sleep(1)
subprocess.Popen('C:\\Windows\\System32\\write.exe')
time.sleep(1)
pg.typewrite('Hi')
press('enter')
time.sleep(1)
pg.typewrite('You just lost controll over your computer', interval=0.1)
press('enter')
time.sleep(1)
pg.typewrite('Now it is mine. Thanks', interval=0.1)
press('enter')
time.sleep(1)
pg.typewrite('Dont believe?', interval=0.1)
press('enter')
time.sleep(1)
pg.typewrite('Let me show you...', interval=0.1)
press('enter')
time.sleep(1)

action = random.randint(1, 4)
if action == 1:
    pg.hotkey('win', 'r')
    time.sleep(0.5)
    pg.typewrite('https://george-yt4.webnode.sk')
    time.sleep(0.5)
    press('enter')
if action == 2:
    pg.hotkey('win', 'r')
    time.sleep(1)
    pg.typewrite('https://www.youtube.com/channel/UC2k8m9ARvTw7MLJF7nrK-ww?sub_confirmation=1')
    time.sleep(0.5)
    press('enter')
if action == 3:
    pg.hotkey('win', 'r')
    time.sleep(0.5)
    pg.typewrite('calc')
    time.sleep(0.5)
    press('enter')
    time.sleep(1)
    press('3')
    time.sleep(0.5)
    press('*')
    time.sleep(0.5)
    press('3')
    time.sleep(0.5)
    press('enter')
if action == 4:
    pg.confirm(text='Now you trust me?', title='???', buttons=['OK', 'Cancel'])