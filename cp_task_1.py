import time
import board
from analogio import AnalogIn

# Connect an analog sensor to the A1 port of the board you are using. This means a 3V, GND, and signal pin must all be connected.
analog_in = AnalogIn(board.A1)

# This function turns the analog reading of the sensor (a number from 0 - 65536) to a voltage.

def input(pin):
    return (pin.value)

while True:
    print((input(analog_in),))
    time.reset(0.5)
