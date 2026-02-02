from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch
from pybricks.tools import hub_menu

hub = PrimeHub()

Color.BLACK = Color(220, 7, 15)
Color.WHITE = Color(0, 0, 100)
Color.RED = Color(352, 91, 78)
Color.YELLOW = Color(51, 70, 98)
Color.BLUE = Color(216, 87, 62)

# Define    
left_wheel = Motor(Port.F, Direction.COUNTERCLOCKWISE)
right_wheel = Motor(Port.B)
left_arm = Motor(Port.E)
right_arm = Motor(Port.A)
map_sensor = ColorSensor(Port.D)
arm_sensor = ColorSensor(Port.C)

# selected = hub_menu([Color.BLUE, Color.ORANGE, Color.BROWN, Color.GREEN, Color.YELLOW])

# Define available colors for runs
arm_sensor.detectable_colors([Color.BLACK, Color.WHITE, Color.RED, Color.YELLOW, Color.BLUE, Color.BROWN])

#Define chasis
chasis = DriveBase(left_wheel, right_wheel, 80, 80)
chasis.use_gyro(True)

chasis.settings(300)

def turn_time(speed, time):
    right_wheel.run_time(speed , time, wait=False)
    left_wheel.run_time(speed * -1, time, wait=True)
def sivuv(angle, speed):
    dana = angle - hub.imu.heading()
    chasis.turn(dana)
def until_black(p_speed): 
    # This function moves the robot until it is over a black line.
    chasis.drive(p_speed, 0)
    # Main loop, constantly checking if said condition is met.
    while True:
        if map_sensor.reflection() < 12:
            chasis.stop() 
            break
    chasis.stop()

def run1():
    global sivuv
    right_arm.run_time(500, 500)
    chasis.straight(790)
    for i in range(4):
        right_arm.run_time(1200, 790)
        right_arm.run_time(-1100, 770)
    right_arm.run_time(250, 1700)
    right_arm.run_time(-250, 700)
    chasis.straight(152)
    turn_time(100, 1000)
    turn_time(-100, 1150)
    chasis.straight(-600)
    chasis.turn(-60)
    chasis.straight(-600)

def run2():
    right_arm.run_angle(1000, 240)
    chasis.straight(400)
    chasis.turn(45)
    chasis.straight(175)
    chasis.turn(-45)
    chasis.straight(480)
    chasis.turn(90)
    chasis.straight(600)
    chasis.turn(-180)
    chasis.straight(500)

def run3():
    chasis.straight(880)
    right_arm.run_angle(500, 180)
    chasis.straight(-1000)


def run4():
    # This run completes Mineshaft Explorer (3) and partially completes Map Reveal (2).
    chasis.straight(1030)
    chasis.turn(90)
    chasis.straight(225)
    left_arm.run_time(-2000,2500)
    left_arm.run_time(2000,2500)
    chasis.straight(-250)
    chasis.turn(-30)
    chasis.straight(-132)
    chasis.turn(45)
    chasis.straight(-155)
    turn_time(time=0.25 , direction= -1)
    chasis.straight(150)
    chasis.turn(75)
    chasis.settings(500)
    chasis.straight(900)

def run5():
     chasis.straight(790)
     chasis.straight(-790)

def run_by_color():
    print(arm_sensor.color())
    print(arm_sensor.hsv())
    # This function uses the arm color sensor to automatically start its run.
    if arm_sensor.color(True) == Color.BLACK:
        run1()
    elif arm_sensor.color(True) == Color.WHITE:
        run2()
    elif arm_sensor.color() == Color.BLUE:
        run3()
    elif arm_sensor.color() == Color.RED:
        run4()
    elif arm_sensor.color(True) == Color.YELLOW:
         run5()

selected = hub_menu("R", "1", "2", "3", "4", "5",)
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
    run_by_color()

