from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch
from pybricks.tools import hub_menu

hub = PrimeHub()

left_arm = Motor(Port.E)
right_arm = Motor(Port.A, Direction.COUNTERCLOCKWISE)
right_wheel = Motor(Port.B)
left_wheel = Motor(Port.F, Direction.COUNTERCLOCKWISE)

chasis = DriveBase(left_wheel, right_wheel, 80, 80)
chasis.use_gyro(True)

chasis.settings(300)

selected = hub_menu("1", "2", "3", "4", "5")


def run1():
    chasis.straight(550)
    for i in range(4):
        right_arm.run_time(1000, 1500)
        right_arm.run_time(1000, 1500)
    chasis.turn(-40)
    chasis.straight(85)
    chasis.turn(40)
    chasis.straight(220)
def run2():
    chasis.straight(600)
    chasis.turn(90)
    chasis.straight(100)
    chasis.turn(-90)
    chasis.straight(50)
    
    chasis.straight(-150)
    chasis.straight(100)
    chasis.straight(-100)
    chasis.straight(100)
    chasis.straight(-100)
    chasis.straight(100)
    chasis.straight(-100)
    chasis.straight(100)
    chasis.straight(-100)
    chasis.straight(100)
    # chasis.straight(200)
    # chasis.straight(-200)

def run3():
    chasis.straight(600)
    chasis.settings(300, straight_acceleration=2000)
    chasis.straight(400)
    right_arm.run_angle(500, -240)
    chasis.settings(300)
    chasis.straight(-820)


def run5():
    # chasis.settings(500)
    # chasis.straight(920)
    # chasis.turn(90)
    # chasis.straight(425)
    # chasis.turn(-90)
    # left_arm.run_time(-2000,2500)
    # left_arm.run_time(2000,2500)
    right_arm.run_time(300, 5000)
    chasis.settings(300)

if selected == "1":
    run1()

if selected == "2":
    run2()

if selected == "3":
    run3()

if selected == "5":
    run5()
