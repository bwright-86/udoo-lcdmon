import sys
import os
sys.path.append('./Adafruit_CharLCD')
from Adafruit_CharLCD import Adafruit_CharLCD
from time import sleep
import psutil

lcd = Adafruit_CharLCD()
#cpu_usage = psutil.cpu_percent()
#ram_usage = psutil.virtual_memory().percent
while True:
	cpu_usage = psutil.cpu_percent()
	ram_usage = psutil.virtual_memory().percent
	lcd.clear()
	lcd.message('CPU Load  %s%%   \n' % (cpu_usage))
	lcd.message('RAM Used  %s%%   ' % (ram_usage))
	sleep(1)
