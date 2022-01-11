"""! @brief
[file description]
"""

## 
# @mainpage
# @author Kyle Jennings, Zarek Lazowski, William Dorosk
# @date January 11th, 2022

import pyb      # import the pyboard module
import time     # import the time module

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

def pin_setup(pin_num, mode, timer=None, channel=None):
    """!
    Sets up the LED pin with the timer and channel.
    @return A channel object to control Pin A0 with.
    """
    
    #Define the pin to use and input/output type
    pin = pyb.Pin(pin_num, mode)
    
    #Set up the timer used for this pin
    if timer and channel:
        tim2 = pyb.Timer(timer, freq=20000)

        #Set up the channel used, invert the PWM signal to correctly
        #  control the LED, as the cathode is connected to the pin
        ch2 = tim2.channel(channel, pyb.Timer.PWM, pin=pin)
        return ch2
    
    return pin


def main():
    ena = pin_setup(pyb.Pin.board.PA10, pyb.Pin.OUT_PP)
    ena.high()

    in1a = pin_setup(pyb.Pin.board.PB4, pyb.Pin.Out_PP)
    in1a.low()

    in2a = pin_setup(pyb.Pin.board.PB5, pyb.Pin.Out_PP, timer=3, channel=2)
    in2a.pulse_width_percent(50)


if __name__ == '__main__':
    print("Hello World!")
    main()