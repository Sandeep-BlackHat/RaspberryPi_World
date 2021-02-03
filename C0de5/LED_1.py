#SIMPLE PROGRAM TO BLINK A LED USING BREAD-BOARD AND RASPBERRY-PI

#Import libraries(to Import GPIO)
import Rpi.GPIO as GPIO
import time #wait for time

GPIO.setmode(GPIO.BCM) #Broadcom Chip Specific for GPIO pins number not the board given numbers

GPIO.Setwarnings(False) #to remove all the warnings

#Defining pins modes
LEDpin = 21
GPIO.setup(LEDpin,GPIO.OUT) #pin mode as output
#blinking logic
GPIO.output(LEDpin,GPIO.HIGH) 
#GPIO high means : actiavted / 1 / true
#GPIO low means : deactivated / 0 / false

time.sleep(2)
GPIO.output(LEDpin,GPIN.LOW)
