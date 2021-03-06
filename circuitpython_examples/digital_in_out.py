"""CircuitPython Essentials Digital In Out example - modified by Evan Weinberg"""
import time
import board
from digitalio import DigitalInOut, Direction, Pull

# LED setup.
led = DigitalInOut(board.LED)

led.direction = Direction.OUTPUT

# Switch setup
#connected to board.D2
switch = DigitalInOut(board.D2)

switch.direction = Direction.INPUT
switch.pull = Pull.UP

while True:
    # We could also do "led.value = not switch.value"!
    if switch.value:
        led.value = False
    else:
        led.value = True
#if the switch is turned on then the value of the led will be false otherwise its true 
    time.sleep(0.01)  # debounce delay
