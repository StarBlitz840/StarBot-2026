from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch
from pybricks.tools import hub_menu

hub = PrimeHub()

left_wheel = Motor(Port.E, Direction.COUNTERCLOCKWISE)
right_wheel = Motor(Port.A)
left_arm = Motor(Port.B)
right_arm = Motor(Port.F)

chasis = DriveBase(left_wheel, right_wheel, 80, 80)
chasis.use_gyro(True)

chasis.settings(500)

runs = hub_menu("1", "2", "3", "4", "5")

def run1():
    chasis.straight(600)
    right_arm.run_time (10000 ,2000 )
    right_arm.run_time (-10000 ,2000 )
# run1()
def run3():

    chasis.straight(880)
    right_arm.run_angle(500, -180)
    chasis.straight(-860)
# run3()

def run5():
    # right_arm.run_time(-300, 5000)
    chasis.straight(920)
    chasis.turn(90)
    chasis.straight(425)
    chasis.turn(-90)
    left_arm.run_time(-2000,2500)
    left_arm.run_time(2000,2500)

if runs == "1":
    run1()

if runs == "3":
    run3()

if runs == "5":
    run5()
run1
