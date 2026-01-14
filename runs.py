from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch
from pybricks.tools import hub_menu

hub = PrimeHub()

left_wheel = Motor(Port.F, Direction.COUNTERCLOCKWISE)
right_wheel = Motor(Port.B)
left_arm = Motor(Port.E)
right_arm = Motor(Port.A)
map_sensor = ColorSensor(Port.D)
arm_sensor = ColorSensor(Port.B)

map_sensor.detectable_colors([Color.BLUE, Color.GRAY, Color.BROWN, Color.ORANGE, Color.RED])

chasis = DriveBase(left_wheel, right_wheel, 80, 80)
chasis.use_gyro(True)

chasis.settings(300)

selected = hub_menu("1", "2", "3", "4", "5", "D")

def until_black(): 
    chasis.drive(100, 0)
    while map_sensor.reflection != 12:
        if map_sensor.color()== Color.NONE:
            break
        print(map_sensor.color())
    chasis.stop()

def run1():
    right_arm.run_time(500, 500)
    chasis.straight(785)
    for i in range(4):
        right_arm.run_time(1000, 770)
        right_arm.run_time(-1000, 735)
    right_arm.run_angle(400, 100)
    until_black()
    chasis.turn(-65)
    chasis.straight(145)
    chasis.turn(-45)
    chasis.straight(95)
    chasis.turn(-100)


def run2(): 
    chasis.straight(-90)
    chasis.straight(90)
    chasis.straight(-90)
    chasis.straight(90)
    chasis.straight(-90)
    chasis.straight(90)
    chasis.straight(-90)
    chasis.straight(90)
    chasis.straight(-90)
    chasis.straight(90)
    chasis.straight(-90)
    chasis.straight(90)
    chasis.straight(-90)
    chasis.straight(90)
    # chasis.straight(200)
    # chasis.straight(-200)

def run3():

    chasis.straight(880)
    right_arm.run_angle(500, -180)
    chasis.straight(-860)


def run4():
    chasis.straight(820)
    chasis.turn(90)
    chasis.straight(425)
    chasis.turn(-90)
    left_arm.run_time(-2000,2500)
    left_arm.run_time(2000,2500)
    right_arm.run_time(-600, 5000)

def run5():
    chasis.straight(790)

def detect_run():
    if arm_sensor.color(True) == Color.BLUE:
        run3()
    #elif

if selected == "1":
    run1()

if selected == "2":
    run2()

if selected == "3":
    run3()

if selected == "4":
    run4()

if selected == "5":
    run5()

if selected == "D":
    detect_run()
