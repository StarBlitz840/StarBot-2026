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

#Define chassis
chassis = DriveBase(left_wheel, right_wheel, 62.4, 80)
chassis.use_gyro(True)

def onboard_diagnosis():
    # Battery diagnosis
    voltage = hub.battery.voltage()     # Read battery voltage (mV)
    amperage = hub.battery.current()    # Read battery current (mA)
    percent = int((voltage - 7000) * 100 // 1200)     # Convert voltage to percentage
    charge = int(amperage * voltage) # Calculate the charge of the battery (mW)
    # Movement accuracy
    


def turn_time(speed, time, p_wait: bool = True):
    right_wheel.run_time(speed , time, wait=False)
    left_wheel.run_time(speed * -1, time, wait=p_wait)

def drive_time(speed, time):
    chassis.drive(speed,0)
    wait(time)

def sivuv(angle, speed):
    dana = angle - hub.imu.heading()
    chassis.turn(dana)

def until_black(p_speed, max_time: int = 10000):
    # This function moves the robot until it is over a black line.
    chassis.drive(p_speed, 0)
    # Main loop, constantly checking if said condition is met.
    while True:
        if map_sensor.reflection() < 12:
            chassis.stop() 
            break
    chassis.stop()

def run1():
    global sivuv
    right_arm.run_time(1000, 500)
    chassis.straight(616)
    for i in range(4):
        right_arm.run_time(1200, 790)
        right_arm.run_time(-1100, 770)
    chassis.straight(109)
    turn_time(100, 1000)
    sivuv(0, 300)
    chassis.straight(-70)
    chassis.turn(-96)
    chassis.straight(-234)
    chassis.straight(390)
    chassis.turn(-45)
    chassis.straight(156)
    chassis.turn(-90)
    chassis.straight(780)

def run2():
    # chassis.settings(straight_speed=100, turn_rate=100)
    chassis.straight(390)
    left_arm.run_angle(1000, -500, wait=False)
    chassis.turn(45)
    chassis.straight(540)
    chassis.turn(45)
    chassis.straight(285)
    chassis.straight(-470)
    chassis.turn(8)
    chassis.straight(-20)
    chassis.turn(-15)
    #sivuv(82, 300)
    #panda blitz is the best team in the בונקר!!!!
    right_arm.run_time(1000, 5000, wait=False)
    turn_time(10, 5000)
    sivuv(90, 300)
    chassis.straight(115)
    left_arm.run_time(-1000, 2000)
    left_arm.run_time(1000, 100)
    sivuv(60, 300)
    chassis.straight(1) # Gives sivuv() time to run.
    chassis.straight(195)
    left_arm.run_time(600, 2000)
    chassis.straight(-300)
    left_arm.run_angle(1000, 300, wait=False)
    sivuv(0, 300)
    chassis.straight(780)
    chassis.turn(-60)
    chassis.straight(780)

def run3():
    # This run completes Mineshaft Explorer (3) and partially completes Map Reveal (2).
    left_arm.run_time(-2000,2500,wait=False)
    chassis.straight(450)
    chassis.curve(300, 45)
    chassis.turn(-90)
    drive_time(300,1500)
    right_arm.run_time(-2000,1500)
    chassis.straight(-200)
    left_arm.run_time(2000,2500,wait=False)
    chassis.turn(135)
    chassis.straight(380)
    chassis.turn(-90)
    chassis.straight(25)
    left_arm.run_time(-2000,2500)
    left_arm.run_time(3000,1500)
    chassis.turn(-90)
    chassis.straight(430)
    chassis.turn(-90)
    chassis.settings(1000)
    chassis.straight(1000)

def run4():
    chassis.straight(647)
    chassis.straight(-180)
    chassis.settings(100)
    chassis.straight(70)
    left_arm.run_time(-300, 1500)
    chassis.straight(-80)
    chassis.settings(600)
    chassis.straight(-1200)

def run5():
    global skip_done
    if skip_done:
        chassis.straight(663)
        chassis.settings(1000)
        chassis.straight(-1560)
        return False
    else:
        chassis.straight(686)
        right_arm.run_angle(500, 180)
        chassis.straight(-780)
        return True

def run_by_color():
    global skip_done
    print(arm_sensor.color())
    print(arm_sensor.hsv())
    # This function uses the arm color sensor to automatically start its run.
    # Reset the heading of the robot.
    hub.imu.reset_heading(0)

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

chassis.settings(300, turn_rate=100)

selected = hub_menu("R", "1", "2", "3", "4", "5")
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