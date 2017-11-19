import curses
import RPi.GPIO as GPIO
import time

frequencyHertz = 30
leftPosition = 0.75
rightPosition = 2.5
middlePosition = (rightPosition - leftPosition) / 2 + leftPosition
positionList = [leftPosition, middlePosition, rightPosition, middlePosition]
msPerCycle = 1000 / frequencyHertz


stdscr = curses.initscr()
curses.cbreak()
stdscr.keypad(1)

stdscr.addstr(0,10,"Hit 'q' to quit")
stdscr.refresh()

def moveForward ():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(12, GPIO.OUT)
    GPIO.setup(11, GPIO.OUT)
    GPIO.setup(13, GPIO.OUT)
    GPIO.setup(15, GPIO.OUT)
    pwmOne = GPIO.PWM(12, frequencyHertz)
    pwmTwo = GPIO.PWM(11, frequencyHertz)
    pwmThree = GPIO.PWM(13, frequencyHertz)
    pwmFour = GPIO.PWM(15, frequencyHertz)
    for position in positionList:
        dutyCyclePercentage = position * 100 / msPerCycle
        pwmOne.start(dutyCyclePercentage)
        time.sleep(.25)
        pwmTwo.start(dutyCyclePercentage)
        time.sleep(.25)
        pwmThree.start(dutyCyclePercentage)
        time.sleep(.25)
        pwmFour.start(dutyCyclePercentage)
        time.sleep(.5)

    pwmOne.stop()
    pwmTwo.stop()
    pwmThree.stop()
    pwmFour.stop()
    GPIO.cleanup()
    return False

key = ''
processing = False

while key != ord('q'):
    key = stdscr.getch()
    if key == curses.KEY_UP:
        
        def processEvent():
            global processing
            if processing == True:
                return
            else:
                processing = True
                processing = moveForward()
            return

        processEvent()
    elif key == curses.KEY_DOWN: 
        stdscr.addstr(3, 20, "Down")


curses.endwin()


