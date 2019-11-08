# SparkFun Electronics
# Experiment 10
# Using the Accelerometer
    
from microbit import *
    
    
class Servo:
    def __init__(self, pin, freq=50, min_us=600, max_us=2400, angle=180):
        self.min_us = min_us
        self.max_us = max_us
        self.us = 0
        self.freq = freq
        self.angle = angle
        self.analog_period = 0
        self.pin = pin
        analog_period = round((1/self.freq) * 1000)  # hertz to miliseconds
        self.pin.set_analog_period(analog_period)
    
    def write_us(self, us):
        us = min(self.max_us, max(self.min_us, us))
        duty = round(us * 1024 * self.freq // 1000000)
        self.pin.write_analog(duty)
        sleep(100)
        self.pin.write_digital(0)  # turn the pin off
    
    def write_angle(self, degrees=None):
        if degrees is None:
            degrees = math.degrees(radians)
        degrees = degrees % 360
        total_range = self.max_us - self.min_us
        us = self.min_us + total_range * degrees // self.angle
        self.write_us(us)
    
# This program demonstrates several input gestures and reacts to them with
# different outputs.

# As recommended, I setup a 6v battery input for the servo, this takes the
# shake out of the servo.

# There are a handful of "gestures" available for the accelerometer. Using
# an endless loop, I have looked for tilt left, tilt right, up, down and shake.

# the output is to turn the servo clockwise, counter clockwise.

# right side and upside down outputs a smile or frown.

# Shake causes a pacman.




    
Servo(pin0).write_angle(0)
while True:
    num = accelerometer.get_x()
    Servo(pin0).write_angle(num * 180 / 2048 + 90) # this turns the servo, now
    # smoothly with the 6v battery

    gesture = accelerometer.current_gesture()
    if gesture == "face up":    # face up is a happy face
        display.show(Image.HAPPY)
    else:
        display.show(Image.ANGRY)   # face down is an angry face

    gesture = accelerometer.current_gesture()
    if gesture == "shake":   # output a pacman on shake
        display.show(Image.PACMAN)
        



    
