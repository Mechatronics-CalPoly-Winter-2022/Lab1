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
#PB6 T4CH1
#PB7 T4CH2

def main():
    '''
    ena = pyb.Pin(pyb.Pin.board.PA10, pyb.Pin.OUT_OD, pyb.Pin.PULL_UP)
    ena.high()

    in1a = pyb.Pin(pyb.Pin.board.PB4, pyb.Pin.OUT_PP)
    tim3 = pyb.Timer(3)
    t3_ch1 = tim3.channel(1, pyb.Timer.PWM, pin=in1a)
    t3_ch1.pulse_width_percent(0)

    in2a = pyb.Pin(pyb.Pin.board.PB5, pyb.Pin.OUT_PP)
    t3_ch2 = tim3.channel(2, pyb.Timer.PWM, pin=in2a)
    t3_ch2.pulse_width_percent(0)
    '''
    
    #Encoder stuff
    '''
    enc1 = pyb.Pin(pyb.Pin.board.PB6, pyb.Pin.AF_PP)
    enc2 = pyb.Pin(pyb.Pin.board.PB7, pyb.Pin.AF_PP)
    
    tim4 = pyb.Timer(4, prescaler=1, period=100000)
    t4_ch1 = tim4.channel(1, pyb.Timer.ENC_A, pin=enc1)
    t4_ch2 = tim4.channel(2, pyb.Timer.ENC_B, pin=enc2)
    '''
    
    enc1 = pyb.Pin(pyb.Pin.board.PC6, pyb.Pin.AF_PP)
    enc2 = pyb.Pin(pyb.Pin.board.PC7, pyb.Pin.AF_PP)
    
    tim8 = pyb.Timer(8, prescaler=1, period=100000)
    t4_ch1 = tim8.channel(1, pyb.Timer.ENC_A, pin=enc1)
    t4_ch2 = tim8.channel(2, pyb.Timer.ENC_B, pin=enc2)
    
    while True:
        time.sleep(0.05)
        print("Encoder 1: ", tim8.counter())


if __name__ == '__main__':
    print("Hello World!")
    main()