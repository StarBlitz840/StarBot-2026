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

chasis = DriveBase(left_wheel, right_wheel, 80, 80)
chasis.use_gyro(True)

chasis.settings(300)

def until_black(): 
    chasis.drive(100, 0)
    while map_sensor.color() != Color.BLACK:
        if map_sensor.color()== Color.BLACK:
            break
    chasis.stop()

def run1():
    right_arm.run_time(500, 500)
    chasis.straight(790)
    for i in range(4):
        right_arm.run_time(1200, 790)
        right_arm.run_time(-1100, 770)
    right_arm.run_time(250, 1700)
    right_arm.run_time(-250, 700)
    chasis.straight(150)
    chasis.turn(-56)
    chasis.straight(215)
    chasis.straight(-25)
    chasis.turn(-25)
    chasis.turn(25)
    chasis.turn(45)
    chasis.straight(30)
    chasis.straight(-1000)
def run2():
    chasis.straight(400)
    chasis.turn(45)
    chasis.straight(175)
    chasis.turn(-35)
    chasis.straight(480)
    chasis.turn(71)
    chasis.straight(400)
    chasis.turn(-180)
    chasis.straight(300)
    chasis.turn(25)
    chasis.straight(185)
    chasis.turn(-40)
    chasis.turn(50)
    chasis.turn(-40)
    chasis.turn(70)
    chasis.turn(-40)
    chasis.turn(70)
def run3():
    chasis.straight(880)
    right_arm.run_angle(500, 180)
    chasis.straight(-1000)
def run4():
    chasis.straight(820)
    chasis.turn(90)
    chasis.straight(425)
    chasis.turn(-90)
    chasis.straight(110)
    left_arm.run_time(speed=-2000,time=2500)
    left_arm.run_time(2000,2500)
    chasis.straight(-110)
    chasis.turn(90)
    chasis.straight(-530)
    chasis.turn(45)
    chasis.straight(-290)
    chasis.straight(290)
    #chasis.turn(45)
    chasis.straight(850)    
def run5():
     chasis.straight(790)
     chasis.straight(-790)
def detect_run():
    # if arm_sensor.color(True) == Color.BLUE:
    #     run1()
    # if arm_sensor.color(True) == Color.BLUE:
    #     run2()
    if arm_sensor.color() == Color.BLUE:
        run3()
    if arm_sensor.color() == Color.RED:
        run4()
    if arm_sensor.color() == Color.YELLOW:
        run5()

# while True:
#     print(arm_sensor.color())

selected = hub_menu("1", "2", "3", "4", "5", "R")
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

if selected == "R":
    detect_run()

