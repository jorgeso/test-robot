import curses
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
global position
position = 1.625 #middle

GPIO.setup(12, GPIO.OUT)
GPIO.setup(11, GPIO.OUT)

frequencyHertz = 50
pwmOne = GPIO.PWM(12, frequencyHertz)
pwmTwo = GPIO.PWM(11, frequencyHertz)

msPerCycle = 1000 / frequencyHertz

dutyCyclePercentage = position * 100 / msPerCycle
print "Position: " + str(position)
print "Duty Cycle: " + str(dutyCyclePercentage) + "%"
print ""
pwmOne.start(dutyCyclePercentage)
time.sleep(0.25)
pwmTwo.start(dutyCyclePercentage)
time.sleep(1)


while position > 1.2:
    global position
    position = position - 0.05

    dutyCyclePercentage = position * 100 / msPerCycle
    print "Position: " + str(position)
    print "Duty Cycle: " + str(dutyCyclePercentage) + "%"
    print ""
    pwmOne.start(dutyCyclePercentage)
    time.sleep(.05)

time.sleep(.5)

pwmOne.stop()
position = 1.625 #middle

while position > 1.2:
    global position
    position = position - 0.05

    dutyCyclePercentage = position * 100 / msPerCycle
    print "Position: " + str(position)
    print "Duty Cycle: " + str(dutyCyclePercentage) + "%"
    print ""
    pwmTwo.start(dutyCyclePercentage)
    time.sleep(.05)

pwmTwo.stop()

GPIO.cleanup()    
    
