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

    _ena: 'pyb.Pin'
    _ch1: 'pyb.Timer.channel'
    _ch2: 'pyb.Timer.channel'

    def __init__(self, en_pin: str, in1pin: str, in2pin: str, timer: 'pyb.Timer'):
        '''! 
        Creates a motor driver by initializing GPIO
        pins and turning the motor off for safety. 
        @param en_pin The pin to which the enable signal
        @param in1pin Counter-clockwise pin ...?
        @param in2pin Clockwise pin ...?
        @param timer The timer to use for PWM
        '''
        print('Creating a motor driver...', end=' ')

        # activate motor
        self._ena = pyb.Pin(en_pin, pyb.Pin.OUT_OD, pyb.Pin.PULL_UP)

        in1a = pyb.Pin(in1pin, pyb.Pin.OUT_PP)
        self._ch1 = timer.channel(1, pyb.Timer.PWM, pin=in1a)
        self._ch1.pulse_width_percent(0)

        in2a = pyb.Pin(in2pin, pyb.Pin.OUT_PP)
        self._ch2 = timer.channel(2, pyb.Timer.PWM, pin=in2a)
        self._ch2.pulse_width_percent(0)

        self.disable_motor()
        
        print('finished.')

    def enable_motor(self):
        '''!
        This method enables the motor.
        '''
        print('Enabling motor...')
        self._ena.high()

    def disable_motor(self):
        '''!
        This method disables the motor.
        '''
        print('Disabling motor...')
        self._ena.low()

    def set_duty_cycle(self, level: int):
        '''!
        This method sets the duty cycle to be sent
        to the motor to the given level. Positive values
        cause torque in one direction, negative values
        in the opposite direction.
        @param level A signed integer holding the duty
                cycle of the voltage sent to the motor 
        '''
        print('Setting duty cycle to ' + str(level))

        # spin counter-clockwise
        if level < 0:
            self._ch1.pulse_width_percent(-level)
            self._ch2.pulse_width_percent(0)
        # spin clockwise
        elif level > 0:
            self._ch1.pulse_width_percent(0)
            self._ch2.pulse_width_percent(level)
        # stop
        else:
            self._ch1.pulse_width_percent(0)
            self._ch2.pulse_width_percent(0)

#PB6 T4CH1
#PB7 T4CH2

def main():
    moe = MotorDriver('PA10', 'PB4', 'PB5', pyb.Timer(3))
    moe.set_duty_cycle(-42)

if __name__ == '__main__':
    print("Hello World!")
    main()