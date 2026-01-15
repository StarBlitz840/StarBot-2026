from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch
from pybricks.tools import hub_menu

hub = PrimeHub()

# Define attatchments
left_wheel = Motor(Port.F, Direction.COUNTERCLOCKWISE)
right_wheel = Motor(Port.B)
left_arm = Motor(Port.E)
right_arm = Motor(Port.A)
map_sensor = ColorSensor(Port.D)
arm_sensor = ColorSensor(Port.C)

# Define available colors for runs
arm_sensor.detectable_colors([Color.BLUE, Color.ORANGE, Color.GREEN, Color.BROWN, Color.YELLOW])

#Define chasis
chasis = DriveBase(left_wheel, right_wheel, 80, 80)
chasis.use_gyro(True)

chasis.settings(300)

#Define available runs
selected = hub_menu("R", "1", "2", "3", "4", "5", "6", "7")
# selected = hub_menu([Color.BLUE, Color.ORANGE, Color.BROWN, Color.GREEN, Color.YELLOW])

def until_black(p_speed): 
    # This function moves the robot until it is over a black line.
    cycles = 0
    chasis.drive(p_speed, 0)
    # Main loop, constantly checking if said condition is met.
    while True:
        if map_sensor.reflection() < 12:
            chasis.stop()
            break
        cycles += 1
    return cycles

def run1():
    # This run completes the Silo (8) and the Forge (6).
    right_arm.run_time(500, 500)
    chasis.straight(785)
    # Hits the Silo arm 4 times.
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
    # This run completes Tip The scales(10) and partially completes Angler Artifacts (11)
    chasis.straight(400)
    chasis.turn(45)
    chasis.straight(175)
    chasis.turn(-30)
    chasis.straight(600)
    chasis.settings(turn_rate=50)
    chasis.turn(75)
    chasis.straight(475)
    chasis.turn(-170)
    chasis.straight(650)
    chasis.settings(100,150)
    chasis.turn(20)
    # Pushes the pulley trigger ten times.
    for i in range(10):
        chasis.turn(-70)
        chasis.turn(70)
    chasis.straight(-250)
    chasis.turn(50)
    chasis.settings(350,100)
    chasis.straight(1000)

    


def run3():
    # This run completes Salvage Operation (12) and plants a flag.
    chasis.straight(880)
    right_arm.run_angle(500, 180)
    chasis.straight(-1000)


def run5():
    # This run completes Mineshaft Explorer (3) and partially completes Map Reveal (2).
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
     # This run plants a flag.
     chasis.straight(790)
     chasis.straight(-790)

def select_run_by_color():
    print(arm_sensor.color(True))
    # This function uses the arm color sensor to automatically start its run. *STILL IN DEVELOPMENT!*
    if arm_sensor.color(True) == Color.GRAY:
        # run1()
        print # temporary
    elif arm_sensor.color(True) == Color.YELLOW:
        run2()
    elif arm_sensor.color(True) == Color.BLUE:
        run3()
    elif arm_sensor.color(True) == Color.MAGENTA:
        # run4()
        print # Temporary hotfix until we make run4()
    elif arm_sensor.color(True) == Color.ORANGE:
        run5()
    elif arm_sensor.color(True) == Color.BROWN:
        run6()

# This block of code runs functions based on user input.
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

if selected == "7":
    until_black(-100)

if selected == "R":
    select_run_by_color()
