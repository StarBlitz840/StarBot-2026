from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

hub = PrimeHub()

left_wheel = Motor(Port.E, Direction.COUNTERCLOCKWISE)
right_wheel = Motor(Port.A)
right_arm = Motor(Port.F)

chasis = DriveBase(left_wheel, right_wheel, 80, 80)

def run3():
    chasis.straight(880)
    right_arm.run_angle(500, -180)
    chasis.straight(-860)

run3()
