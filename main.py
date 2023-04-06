#!/usr/bin/env pybricks-micropython
import "lib.py"
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile


# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.


# Create your objects here.
ev3 = EV3Brick()
left = Motor(Port.A)
right = Motor(Port.B)
robot = DriveBase(left,right, wheel_diameter=55.5, axle_track=104)
gyro =GyroSensor(Port.1, positive_direction=Direction.CLOCKWISE)
# Write your program here.
robot.settings(70)
robot.straight(600)


