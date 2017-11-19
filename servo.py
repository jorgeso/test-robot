#This gives us control of the Raspberry Pi's pins.
import RPi.GPIO as GPIO

# This is only used for time delays... standard Python stuff.
import time

# tell Pi which pin numbers we'll be using ot refer to the GPIO pins
# we will use the physical pin ordering
GPIO.setmode(GPIO.BOARD)

# We will tell the Broadcom CPU which pins do what.
# There are many pins and most have up to 5 different functions,
# each with a default. Check pinout to find-non-specialized
# "GPIO" pins. We'll use P1_Pin_11 (using BOARD reference),
# which is the same as GPI017 (Broadcom / BCM reference).
# We still just need it to use the GPIO digital function, we just
# need to tell it to designate this pint for OUTPUT
GPIO.setup(12, GPIO.OUT)
GPIO.setup(11, GPIO.OUT)

# Now we can use PWM on pin 11. It's software PWM, so don't expect perfect
# results. Linux is a multitasking OS so other processes could interrupt
# the process which generates the PWM signal at any time.
# Raspberry Pi has a hardware PWM channel, but this Python library
# does not yet support it.

# Create a PWM control object.
# 12 is the output pin
# 50 is the cycle frequency in Hertz
frequencyHertz = 50
pwmOne = GPIO.PWM(12, frequencyHertz)
pwmTwo = GPIO.PWM(11, frequencyHertz)

# How to position a servo? All servos are pretty much the same.
# Send repeated pulses of an absolute duration (not a relative duty cycle)
# between 0.75 ms and 2.5 ms in duration. A single pulse will continue
# its movement and then once it arrives at the specified position, will
# instruct the motor to forcefully hold its position.

# How to calculate the duty cycle for specific duration
# First, know the pulse time for the position you want
leftPosition = 0.75
rightPosition = 2.5
middlePosition = (rightPosition - leftPosition) / 2 + leftPosition

# I'll store a sequence of positions for use in a loop later on
positionList = [leftPosition, middlePosition, rightPosition, middlePosition]

# Total number of milliseconds in a cycle. Given this, we will then
# know both how long we want to pulse in this cycle and how long the
# cycle itself is. That is all we need to calculate a duty cycle as
# a percentage
msPerCycle = 1000 / frequencyHertz

for i in range(3):
    # this sequence contains positions form left to right
    # and then back again. Move the motor to each position order.
    for position in positionList:
        dutyCyclePercentage = position * 100 / msPerCycle
        print "Position: " + str(position)
        print "Duty Cycle: " + str(dutyCyclePercentage) + "%"
        print ""
        pwmOne.start(dutyCyclePercentage)
        time.sleep(.25)
        pwmTwo.start(dutyCyclePercentage)
        time.sleep(.5)

# Done. Terminate all signals and relax the motor.
pwmOne.stop()
pwmTwo.stop()

# We have shut all our stuff down but we should do a complete
# close on all GPIO stuff. There's only one copy of real hardware.
# We need to be polite and put it back the way we found it.
GPIO.cleanup()
