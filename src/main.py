"""! @brief
[file description]
"""

## 
# @mainpage
# @author Kyle Jennings, Zarek Lazowski, William Dorosk
# @date January 11th, 2022

import pyb      # import the pyboard module
import time     # import the time module

"""
class MotorDriver:
    '''! 
    This class implements a motor driver for an ME405 kit. 
    '''

    def __init__(self, en_pin, in1pin, in2pin, timer):
        '''! 
        Creates a motor driver by initializing GPIO
        pins and turning the motor off for safety. 
        @param en_pin ...
        @param in1pin ...
        @param in2pin ...
        @param timer ...
        '''
        print('Creating a motor driver...', end=' ')

        print('finished.')

    def set_duty_cycle(self, level):
        '''!
        This method sets the duty cycle to be sent
        to the motor to the given level. Positive values
        cause torque in one direction, negative values
        in the opposite direction.
        @param level A signed integer holding the duty
                cycle of the voltage sent to the motor 
        '''
        print('Setting duty cycle to ' + str(level))
"""


def main():
    ena = pyb.Pin(pyb.Pin.board.PA10, pyb.Pin.OUT_OD, pyb.Pin.PULL_UP)
    ena.high()

    in1a = pyb.Pin(pyb.Pin.board.PB4, pyb.Pin.OUT_PP)
    tim3 = pyb.Timer(3, freq=20000)
    ch1 = tim3.channel(1, pyb.Timer.PWM, pin=in1a)
    ch1.pulse_width_percent(0)

    in2a = pyb.Pin(pyb.Pin.board.PB5, pyb.Pin.OUT_PP)
    ch2 = tim3.channel(2, pyb.Timer.PWM, pin=in2a)
    ch2.pulse_width_percent(0)


if __name__ == '__main__':
    print("Hello World!")
    main()