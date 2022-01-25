"""! 
@brief This file offers classes for both controlling motors
and reading values from encoders.
"""

## 
# @mainpage
# @section description_main Lab 1
# This is the documentation page for Lab 0, a program that
# offers a driver for running motors and reading encoders.
#
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
        @brief This method enables the motor.
        '''
        print('Enabling motor...')
        self._ena.high()

    def disable_motor(self):
        '''!
        @brief This method disables the motor.
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

class EncoderDriver:
    '''!
    This class implements an encoder driver for an ME405 kit.
    '''

    _pin1: 'pyb.Pin'
    _pin2: 'pyb.Pin'
    _tim: 'pyb.Timer'
    _ch1: 'pyb.Timer.channel'
    _ch2: 'pyb.Timer.channel'

    def __init__(self, enc_1: str, enc_2: str, timer: 'pyb.Timer') -> None:
        '''!
        Creates an encoder driver by initializing GPIO pins
        @param enc_1 The pin to which the first encoder signal
        @param enc_2 The pin to which the second encoder signal
        @param timer The timer to use for the encoder
        '''
        self._pin1 = pyb.Pin(enc_1, pyb.Pin.AF_PP)
        self._pin2 = pyb.Pin(enc_2, pyb.Pin.AF_PP)
        self._tim = timer
        self._tim.prescaler(1)
        self._tim.period(100000)

        self._ch1 = self._tim.channel(1, pyb.Timer.ENC_A, pin=self._pin1)
        self._ch2 = self._tim.channel(2, pyb.Timer.ENC_B, pin=self._pin2)

    def get_count(self) -> int:
        '''!
        This method returns the current count of the encoder.
        @return The current count of the encoder
        '''
        return self._tim.counter()


def main():
    moe = MotorDriver('PA10', 'PB4', 'PB5', pyb.Timer(3))
    enc = EncoderDriver('PB6', 'PB7', pyb.Timer(8))
    moe.set_duty_cycle(-42)

    while True:
        time.sleep(0.05)
        print("Encoder 1: ", enc.get_count())


if __name__ == '__main__':
    print("Hello World!")
    main()