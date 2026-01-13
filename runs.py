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
arm_sensor = ColorSensor(Port.C)

arm_sensor.detectable_colors([Color.BLUE, Color.ORANGE, Color.BROWN, Color.GRAY, Color.YELLOW])

chasis = DriveBase(left_wheel, right_wheel, 80, 80)
chasis.use_gyro(True)

chasis.settings(300)

selected = hub_menu("1", "2", "3", "4", "5", "6")

def until_black(): 
    while True:
        chasis.drive(100, 0)
        if map_sensor.reflection() < 12:
            break
    chasis.stop()

def run1():
    right_arm.run_time(500, 500)
    chasis.straight(785)
    for i in range(4):
     right_arm.run_time(1200, 790)
     right_arm.run_time(-1100, 755)
    right_arm.run_time(250, 1700)
    right_arm.run_time(-250, 700)
    chasis.straight(150)
    chasis.turn(-56)
    chasis.straight(215)
    chasis.turn(45)
    chasis.straight(-1000)
    
    
    



def run2():
    chasis.straight(400)
    chasis.turn(45)
    chasis.straight(175)
    chasis.turn(-30)
    chasis.straight(220)
    chasis.turn(80)
    chasis.straight(400)
    chasis.straight(-200)
    chasis.turn(-90)
    until_black()
    


def run3():

    chasis.straight(880)
    right_arm.run_angle(500, 180)
    chasis.straight(-1000)


def run5():
    chasis.straight(820)
    chasis.turn(90)
    chasis.straight(425)
    chasis.turn(-90)
    chasis.straight(110)
    left_arm.run_time(-2000,2500)
    left_arm.run_time(2000,2500)
    chasis.straight(-110)
    chasis.turn(90)
    chasis.straight(-530)
    chasis.turn(45)
    chasis.straight(-290)
    chasis.straight(290)
    chasis.turn(45)
    chasis.straight(850)

def run6():
     chasis.straight(790)
     chasis.straight(-790)


if selected == "1":
    while True:
        run1()

if selected == "2":
    run2()

if selected == "3":
    run3()

if selected == "5":
    run5()

if selected == "6":
    run6()