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
    right_arm.run_time(500, 500)
    chasis.straight(790)
    for i in range(4):
        right_arm.run_time(1200, 790)
        right_arm.run_time(-1100, 770)
    right_arm.run_time(250, 1700)
    right_arm.run_time(-250, 700)
    chasis.straight(135)
    turn_time(300, 2000)
    turn_time(-300, 2000)
    chasis.turn(50)
    chasis.straight(-1000)
    chasis.turn(-90)
    chasis.straight(-400)

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
    chasis.turn(25)
    chasis.straight(200)
    right_arm.run_angle(1000, 180)
    for i in range(10):
        turn_time(700, -70)
        turn_time(600, 70)
    chasis.turn(-15)
    until_black(-300)
    chasis.turn(90)
    chasis.straight(300)
    chasis.turn(45)
    right_arm.run_angle(1000, -420)
    chasis.straight(400)
    right_arm.run_time(1000, 600)
    until_black(-300)

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
    # This function uses the arm color sensor to automatically start its run. *STILL IN DEVELOPMENT!*
    if arm_sensor.color(True) == Color.BLACK:
        run1()
        print # temporary
    elif arm_sensor.color(True) == Color.WHITE:
        run2()
    elif arm_sensor.color(True) == Color.BLUE:
        run3()
    elif arm_sensor.color(True) == Color.RED:
        run4()
    elif arm_sensor.color(True) == Color.YELLOW:
        # run5()
        print # Temporary hotfix until we make run5()

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

