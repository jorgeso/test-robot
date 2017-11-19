import curses
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
middlePosition = 1.625
leftSideForwardPosition = 1.4
rightSideBackPosition = 1.4
leftSideBackPosition = 1.9
rightSideForwardPosition = 1.9

frequencyHertz = 50
msPerCycle = 1000 / frequencyHertz

global frontLeftPosition
global backLeftPosition
global frontRightPosition
global backRightPosition

global backLeftdutyCyclePercentage
global frontLeftdutyCyclePercentage
global frontRightdutyCyclePercentage
global backRightdutyCyclePercentage

GPIO.setup(11, GPIO.OUT)
frontLeftLeg = GPIO.PWM(11, frequencyHertz)

GPIO.setup(15, GPIO.OUT)
frontRightLeg = GPIO.PWM(15, frequencyHertz)

GPIO.setup(12, GPIO.OUT)
backLeftLeg = GPIO.PWM(12, frequencyHertz)

GPIO.setup(13, GPIO.OUT)
backRightLeg = GPIO.PWM(13, frequencyHertz)

def moveLegsToMiddle ():
    global frontLeftPosition
    global backLeftPosition
    global frontRightPosition
    global backRightPosition
    global backLeftdutyCyclePercentage
    global frontLeftdutyCyclePercentage
    global frontRightdutyCyclePercentage
    global backRightdutyCyclePercentage
    frontLeftPosition = middlePosition
    backLeftPosition = middlePosition
    frontRightPosition = middlePosition
    backRightPosition = middlePosition
    backLeftdutyCyclePercentage = backLeftPosition * 100 / msPerCycle
    frontLeftdutyCyclePercentage = frontLeftPosition * 100 / msPerCycle
    frontRightdutyCyclePercentage = frontRightPosition * 100 / msPerCycle
    backRightdutyCyclePercentage = backRightPosition * 100 / msPerCycle
    frontLeftLeg.start(frontLeftdutyCyclePercentage)
    time.sleep(.25)

    frontRightLeg.start(frontRightdutyCyclePercentage)
    time.sleep(.25)

    backLeftLeg.start(backLeftdutyCyclePercentage)
    time.sleep(.25)

    backRightLeg.start(backRightdutyCyclePercentage)
    time.sleep(.25)
    return

moveLegsToMiddle()

def frontLeftForward ():
    global frontLeftPosition
    global frontLeftdutyCyclePercentage
    while frontLeftPosition > leftSideForwardPosition:
        frontLeftPosition = frontLeftPosition - 0.05

        frontLeftdutyCyclePercentage = frontLeftPosition * 100 / msPerCycle
        print "Front Left Position: " + str(frontLeftPosition)
        print "Front Left Duty Cycle: " + str(frontLeftdutyCyclePercentage) + "%"
        print ""
        frontLeftLeg.start(frontLeftdutyCyclePercentage)
        time.sleep(.05)
    return

frontLeftForward()

global otherLegsMovement
otherLegsMovement = 0

while otherLegsMovement < 0.275:

    if backLeftPosition < leftSideBackPosition:
        backLeftPosition = backLeftPosition + 0.05
        backLeftdutyCyclePercentage = backLeftPosition * 100 / msPerCycle
        print "Back Left Position: " + str(frontLeftPosition)
        print "Back Left Duty Cycle: " + str(frontLeftdutyCyclePercentage) + "%"
        print ""
        backLeftLeg.start(backLeftdutyCyclePercentage)
        time.sleep(.05)

    frontRightPosition = frontRightPosition - 0.05
    frontRightdutyCyclePercentage = frontRightPosition * 100 / msPerCycle
    print "Front Right Position: " + str(frontLeftPosition)
    print "Front Right Duty Cycle: " + str(frontLeftdutyCyclePercentage) + "%"
    print ""
    frontRightLeg.start(frontRightdutyCyclePercentage)
    time.sleep(.05)

    backRightPosition = backRightPosition - 0.05
    backRightdutyCyclePercentage = backRightPosition * 100 / msPerCycle
    print "Back Right Position: " + str(frontLeftPosition)
    print "Back Right Duty Cycle: " + str(frontLeftdutyCyclePercentage) + "%"
    print ""
    backRightLeg.start(backRightdutyCyclePercentage)
    time.sleep(.05)

    otherLegsMovement = otherLegsMovement + 0.05

time.sleep(.5)


while frontRightPosition < rightSideForwardPosition:
    
    frontRightPosition = frontRightPosition + 0.05

    frontRightdutyCyclePercentage = frontRightPosition * 100 / msPerCycle
    print "Front Right Position: " + str(frontRightPosition)
    print "Front Right Duty Cycle: " + str(frontRightdutyCyclePercentage) + "%"
    print ""
    frontRightLeg.start(frontRightdutyCyclePercentage)
    time.sleep(.05)

while backLeftPosition > leftSideForwardPosition:
    
    backLeftPosition = backLeftPosition - 0.05

    backLeftdutyCyclePercentage = backLeftPosition * 100 / msPerCycle
    print "Back Left Position: " + str(backLeftPosition)
    print "Back Left Duty Cycle: " + str(backLeftdutyCyclePercentage) + "%"
    print ""
    backLeftLeg.start(backLeftdutyCyclePercentage)
    time.sleep(.05)

while backRightPosition < rightSideForwardPosition:
    
    backRightPosition = backRightPosition + 0.05

    backRightdutyCyclePercentage = backRightPosition * 100 / msPerCycle
    print "Back Right Position: " + str(backRightPosition)
    print "Back Right Duty Cycle: " + str(backRightdutyCyclePercentage) + "%"
    print ""
    backRightLeg.start(backRightdutyCyclePercentage)
    time.sleep(.05)

otherLegsMovement = 0

while otherLegsMovement < 0.275:

    if frontLeftPosition < middlePosition:
        frontLeftPosition = frontLeftPosition + 0.05

        frontLeftdutyCyclePercentage = frontLeftPosition * 100 / msPerCycle
        print "Front Left Position: " + str(frontLeftPosition)
        print "Front Left Duty Cycle: " + str(frontLeftdutyCyclePercentage) + "%"
        print ""
        frontLeftLeg.start(frontLeftdutyCyclePercentage)
        time.sleep(.05)

    if backLeftPosition < middlePosition:
        backLeftPosition = backLeftPosition + 0.05
        backLeftdutyCyclePercentage = backLeftPosition * 100 / msPerCycle
        print "Back Left Position: " + str(frontLeftPosition)
        print "Back Left Duty Cycle: " + str(frontLeftdutyCyclePercentage) + "%"
        print ""
        backLeftLeg.start(backLeftdutyCyclePercentage)
        time.sleep(.05)

    if frontRightPosition > middlePosition:
        frontRightPosition = frontRightPosition - 0.05
        frontRightdutyCyclePercentage = frontRightPosition * 100 / msPerCycle
        print "Front Right Position: " + str(frontLeftPosition)
        print "Front Right Duty Cycle: " + str(frontLeftdutyCyclePercentage) + "%"
        print ""
        frontRightLeg.start(frontRightdutyCyclePercentage)
        time.sleep(.05)

    if backRightPosition > middlePosition:
        backRightPosition = backRightPosition - 0.05
        backRightdutyCyclePercentage = backRightPosition * 100 / msPerCycle
        print "Back Right Position: " + str(frontLeftPosition)
        print "Back Right Duty Cycle: " + str(frontLeftdutyCyclePercentage) + "%"
        print ""
        backRightLeg.start(backRightdutyCyclePercentage)
        time.sleep(.05)

    otherLegsMovement = otherLegsMovement + 0.05


time.sleep(.5)

frontLeftLeg.stop()
frontRightLeg.stop()
backLeftLeg.stop()
backRightLeg.stop()

GPIO.cleanup()
