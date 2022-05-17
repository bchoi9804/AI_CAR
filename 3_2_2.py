import RPi.GPIO as GPIO
import time

SW1 = 5

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(SW1,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)

oldSw = 0
newSw = 0

try:
    while True:
        newSw = GPIO.input(SW1)
        if newSw != oldSw:
            oldSw = newSw
            print("click")
            time.sleep(0.2)

except KeyboardInterrupt:
    pass

GPIO.cleanup()