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

# Set up 2 part run.
skip_done = False

# selected = hub_menu([Color.BLUE, Color.ORANGE, Color.BROWN, Color.GREEN, Color.YELLOW])

# Define available colors for runs
arm_sensor.detectable_colors([Color.BLACK, Color.WHITE, Color.RED, Color.YELLOW, Color.BLUE, Color.BROWN])

#Define chasis
chasis = DriveBase(left_wheel, right_wheel, 80, 80)
chasis.use_gyro(True)

chasis.settings(300, turn_rate=100)

def turn_time(speed, time, p_wait: bool = True):
    right_wheel.run_time(speed , time, wait=False)
    left_wheel.run_time(speed * -1, time, wait=p_wait)

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
    chasis.straight(140)
    turn_time(100, 1000)
    sivuv(0, 300)
    chasis.straight(-90)
    chasis.turn(-96)
    chasis.straight(-300)
    chasis.straight(500)
    chasis.turn(-45)
    chasis.straight(200)
    chasis.turn(-90)
    chasis.straight(1000)

def run2():
    # chasis.settings(straight_speed=100, turn_rate=100)
    chasis.straight(500)
    left_arm.run_angle(1000, -500, wait=False)
    chasis.turn(45)
    chasis.straight(600)
    chasis.turn(45)
    chasis.straight(350)
    turn_time(300, 350)
    chasis.straight(-200)
    sivuv(90, 300)
    turn_time(10, 2000, False)
    until_black(-225)
    sivuv(92, 300)
    chasis.straight(-10)
    sivuv(82, 300)
    right_arm.run_time(1000, 5000, wait=False)
    turn_time(10, 5000)
    sivuv(90, 300)
    chasis.straight(180)
    left_arm.run_time(-1000, 2000)
    # left_arm.run_time(1000, 100)
    sivuv(57, 300)
    chasis.straight(1) # Gives sivuv() time to run.
    chasis.straight(250)
    left_arm.run_time(600, 2000)
    chasis.straight(-425)
    left_arm.run_angle(1000, 300, wait=False)
    sivuv(0, 300)
    chasis.straight(1000)
    chasis.turn(-60, wait=False)
    chasis.straight(1000)

def run5():
    global skip_done
    if skip_done:
        chasis.straight(800)
        chasis.settings(1000)
        chasis.straight(-2000)
        return False
    else:
        chasis.straight(880)
        right_arm.run_angle(500, 180)
        chasis.straight(-1000)
        return True



def run3():
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
    chasis.straight(-150)
    chasis.turn(30)
    chasis.turn(-30)
    chasis.straight(150)
    chasis.turn(45)
    chasis.straight(200)
    chasis.turn(30)
    chasis.straight(600)
    chasis.turn(10)
    chasis.straight(400)

def run4():
     chasis.straight(830)
     chasis.straight(-200)
     chasis.settings(100)
     chasis.straight(50)
     left_arm.run_time(-300, 1500)
     chasis.straight(-100)
     chasis.settings(500)
     chasis.straight(-2000)

def run_by_color():
    global skip_done
    print(arm_sensor.color())
    print(arm_sensor.hsv())
    # This function uses the arm color sensor to automatically start its run.
    # Reset the heading of the robot.
    hub.imu.reset_heading(0)

    sivuv(90, 300)

    if arm_sensor.color(True) == Color.BLACK:
        run1()
    elif arm_sensor.color(True) == Color.WHITE:
        run2()
    elif arm_sensor.color() == Color.RED:
        run3()
    elif arm_sensor.color() == Color.YELLOW:
        run4()
    elif arm_sensor.color(True) == Color.BLUE:
        skip_done = run5()

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
