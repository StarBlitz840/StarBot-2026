from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

hub = PrimeHub()

Left_Wheel = Motor(Port.E, Direction.COUNTERCLOCKWISE)
Right_Wheel = Motor(Port.A, Direction.CLOCKWISE)
Right_Arm = Motor(Port.F)

chasis = DriveBase(Left_Wheel, Right_Wheel, 80, 80)

def ship():
    chasis.straight(860)
    chasis.straight(-860)

ship()
