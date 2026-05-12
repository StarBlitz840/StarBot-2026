from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop, Icon
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
arm_sensor.detectable_colors([Color.BLACK, Color.WHITE, Color.RED, Color.YELLOW, Color.BLUE, Color.GRAY])


#Define chassis
chassis = DriveBase(left_wheel, right_wheel, 62.4, 80)
chassis.use_gyro(True)


def onboard_diagnosis():
    # Battery diagnosis
    voltage = hub.battery.voltage()     # Read battery voltage (mV)
    amperage = hub.battery.current()    # Read battery current (mA)
    percent = int((voltage - 7000) * 100 // 1200)     # Convert voltage to percentage
    charge = int(amperage * voltage) # Calculate the charge of the battery (mW)


    # motor health
    right_arm.run_time(20000, 1000, wait=False)
    left_arm.run_time(20000, 1000, wait=False)
    wait(500)
    right_arm_speed = right_arm.speed()
    left_arm_speed = left_arm.speed()


    # Movement accuracy
    move_dist_before = []
    move_dist_after = []
    move_error = ["Feature defunct // Reason: Erez", "Feature defunct // Reason: Erez", "Feature defunct // Reason: Erez"]
    # tof_sensor = UltrasonicSensor(Port.C)   # Define a Time Of Flight sensor
    # for i in range(3):
    #     if i == 0:  # Test different speeds based on iteration
    #         chassis.settings(300)
    #     if i == 1:
    #         chassis.settings(500)
    #     if i == 2:
    #         chassis.settings(1000)
    #        
    #     move_dist_before.append(tof_sensor.distance())     # Log distance before movement
    #     chassis.straight(20)    # Move 2cm
    #     move_dist_after.append(tof_sensor.distance())      # Log distance after movement
    #     move_error.append((move_dist_before(i) + move_dist_after(i)) / 2)  # Calculate the error in each iteration
   
    # Turn accuracy
    turn_dist_before = []
    turn_dist_after = []
    turn_error = []
    for i in range(3):
        if i == 0:  # Test different speeds based on iteration
            chassis.settings(turn_rate=300)
        if i == 1:
            chassis.settings(turn_rate=500)
        if i == 2:
            chassis.settings(turn_rate=1000)
        chassis.stop()
        hub.imu.reset_heading(0)    # Reset robot heading


        turn_dist_before.append(hub.imu.heading())     # Log heading before movement
        chassis.turn(90)    # Turn 90 degrees
        turn_dist_after.append(hub.imu.heading())      # Log heading after movement
        turn_error.append((turn_dist_after[i] - turn_dist_before[i]) - 90)  # Calculate the error in each iteration
   
    print("Battery percentege: ", percent, "% // Available power: ", charge, "mW\nMovement accuracy:\n" \
    "Standard (300) - Straight: ", move_error[0], " // Turn: ", turn_error[0], "\n" \
    "Fast (500) - Straight: ", move_error[1], " // Turn: ", turn_error[1], "\n" \
    "Ludicrous (1,000) - Straight: ", move_error[2], " // Turn: ", turn_error[2], \
    "\nMotor health:\nRight motor: ", right_arm_speed, " // Left motor: ", left_arm_speed)


def turn_time(speed, time, p_wait: bool = True):
    right_wheel.run_time(speed , time, wait=False)
    left_wheel.run_time(speed * -1, time, wait=p_wait)


def drive_time(speed, time):
    chassis.drive(speed,0)
    wait(time)


def sivuv(angle, speed):
    dana = angle - hub.imu.heading()
    chassis.turn(dana)


def until_black(p_speed, max_dist: int = 10000):
    # This function moves the robot until it is over a black line.
    chassis.drive(p_speed, 0)
    # Main loop, constantly checking if said condition is met.
    while True:
        if map_sensor.reflection() < 12:
            chassis.stop()
            break
    chassis.stop()


def until_white(p_speed, max_dist: int = 10000):
    # This function moves the robot until it is over a white line.
    chassis.drive(p_speed, 0)
    # Main loop, constantly checking if said condition is met.
    while True:
        print(map_sensor.reflection())
        if map_sensor.reflection() > 90:
            chassis.stop()
            break
    chassis.stop()



def color_on():
    brightness = list(range(0, 100, 4)) + list(range(100, 0, -4))
    hub.display.animate([Icon.HEART * i / 100 for i in brightness], 30)
    hub.light.animate([Color.RED, Color.ORANGE, Color.YELLOW, Color.GREEN, Color.CYAN, Color.BLUE, Color.VIOLET, Color.MAGENTA], interval=150)
    while True:
        wait(100)


def chack_button_pressed():
    pressed = []
    while not any(pressed):
        pressed = hub.buttons.pressed()
        wait(10)


    hub.display.icon(Icon.CIRCLE)


    while any(hub.buttons.pressed()):
        wait(10)


    if Button.LEFT in pressed:
        hub.display.icon(Icon.ARROW_LEFT_DOWN)
    elif Button.RIGHT in pressed:
        hub.display.icon(Icon.ARROW_RIGHT_DOWN)
    elif Button.BLUETOOTH in pressed:
        hub.display.icon(Icon.ARROW_RIGHT_UP)
    wait(5000)
   
def we_won():
    hub.display.text("we won! we won!!!")


def shubi_dubi():
    hub.display.text("Shubi Dubi and The Cool Guy...")


def run1():
    global sivuv
    left_arm.run_time(1000, 1500)
    right_arm.run_time(1000, 500, wait=False)
    chassis.straight(605)
    for i in range(4):
        right_arm.run_time(1200, 890)
        right_arm.run_time(-1200, 800)
    sivuv(0, 300)
    chassis.curve(1200, 10)
    if map_sensor.reflection() >= 12:
        chassis.straight(-10)
    sivuv(0, 300)
    turn_time(90, 1000)
    sivuv(0, 300)
    chassis.straight(-60)
    chassis.turn(-95)
    chassis.straight(-150)
    left_arm.run_time(-500, 1000)
    chassis.straight(-175)
    left_arm.run_time(500, 1000, wait=False)
    chassis.settings(1000)
    chassis.straight(400)
    chassis.turn(-90)
    chassis.straight(1000)
    
def run2():
    drive_time(500,1500)
    right_arm.run_time(1000, 2000)
    drive_time(-1000, 1500)
    chassis.straight(1)
    right_arm.run_time(-1000, 2000)
    # right_arm.run_time(-1000, 2000)
    # chassis.settings(100)
    # chassis.straight(50, wait=False)
    # right_arm.run_time(-800, 2000)
    # chassis.settings(500)
    # turn_time(500, 1000)
    # sivuv(0, 300)
    chassis.settings(1000)
    chassis.straight(-2000)

def run3():
    chassis.straight(200)
    chassis.curve(250, 45)
    chassis.curve(250, -45)
    chassis.straight(175)
    until_black(100)
    sivuv(88, -300)
    until_black(-100)
    chassis.straight(15)
    chassis.settings(500)
    right_arm.run_time(1000, 6000, wait=False)
    turn_time(25, 6000)
    sivuv(90, 300)
    chassis.turn(5)
    chassis.straight(130)
    sivuv(0, 300)
    wait(350)
    chassis.straight(-25)
    chassis.turn(40)
    chassis.straight(225)
    left_arm.run_time(-1000, 3000)
    turn_time(-500, 2500)
    turn_time(500, 2500)
    chassis.straight(-200)
    sivuv(0, 300)
    chassis.settings(1000)
    chassis.curve(800, -90)

def run4():
    # This run completes Mineshaft Explorer (3) and Map Reveal (2).
    left_arm.run_time(-2000,2500,wait=False)
    right_arm.run_time(5000,1500,wait=False)
    chassis.straight(475)
    chassis.curve(300, 45)
    chassis.turn(-90)
    drive_time(300,1500)
    right_arm.run_time(-5000,1500)
    chassis.straight(-200)
    left_arm.run_time(2000,2500,wait=False)
    chassis.turn(135)
    chassis.straight(370)
    chassis.turn(-90)
    chassis.straight(40)
    left_arm.run_time(-2000,2500)
    left_arm.run_time(3000,1500)
    chassis.turn(90)
    chassis.straight(-170)
    chassis.settings(1000)
    chassis.curve(-300, 90, then=Stop.NONE)
    chassis.straight(-1000)

def run5():
    left_arm.run_time(300, 1500, wait=None)
    chassis.straight(647)
    chassis.straight(-180)
    chassis.settings(100)
    chassis.straight(75)
    chassis.turn(-7)
    left_arm.run_time(-300, 1500)
    #chassis.straight(-80)
    chassis.settings(1000)
    #chassis.turn(45)
    #chassis.turn(-45)
    chassis.straight(-100)
    chassis.curve(-400, -90, then=Stop.NONE)
    left_arm.run_time(300, 1500)

def run6():
    chassis.straight(663)
    right_arm.run_time(1000, 1000)
    chassis.settings(1000)
    chassis.straight(-1560)

def run7():
    chassis.straight(50)
    chassis.turn(75)
    chassis.straight(400)

# run7()

def run_by_color():
    global skip_done
    print(arm_sensor.color())
    print(arm_sensor.hsv())
    # This function uses the arm color sensor to automatically start its run.
    # Reset the heading of the robot.
    hub.imu.reset_heading(0)
    right_arm.stop()
    left_arm.stop()
    acolor = arm_sensor.color()
    ahsv = arm_sensor.hsv()


    if arm_sensor.color(True) == Color.BLACK:
        hub.display.number(1)
        hub.light.on(ahsv)
        run1()
    elif arm_sensor.color(True) == Color.GRAY:
        hub.display.number(2)
        hub.light.on(ahsv)
        run2()
    elif arm_sensor.color(True) == Color.WHITE:
        hub.display.number(3)
        hub.light.on(ahsv)
        run3()
    elif arm_sensor.color() == Color.RED:
        hub.display.number(4)
        hub.light.on(ahsv)
        run4()
    elif arm_sensor.color() == Color.YELLOW:
        hub.display.number(5)
        hub.light.on(ahsv)
        run5()
    elif arm_sensor.color(True) == Color.BLUE:
        hub.display.number(6)
        hub.light.on(ahsv)
        run6()
   
chassis.settings(500, turn_rate=100)


s = hub.display.icon(Icon.HEART)


# selected = hub_menu("R", "1", "2", "3", "4", "5","W", "C","P","D")
selected = hub_menu("R", "#", "1", "2", "3", "4", "5","S")
if selected == "1":
    hub.light.blink(Color.GREEN, [300, 300])
    run1()
   
if selected == "2":
    hub.light.blink(Color.RED, [300, 300])
    run2()


if selected == "3":
    hub.light.blink(Color.ORANGE, [300, 300])
    run3()


if selected == "4":
    hub.light.blink(Color.WHITE, [300, 300])
    run4()


if selected == "5":
    hub.light.blink(Color.BLUE, [300, 300])
    run5()


if selected == "R":
    run_by_color()


if selected == "#":
    selected3 = hub_menu("5", "4", "3", "2", "1")
    if selected3 == "1":
        while True:
            chassis.drive(speed=200, turn_rate=0)
    if selected3 == "2":
        while True:
            chassis.drive(speed=400, turn_rate=0)
    if selected3 == "3":
        while True:
            chassis.drive(speed=600, turn_rate=0)
    if selected3 == "4":
        while True:
            chassis.drive(speed=800, turn_rate=0)
    if selected3 == "5":
        while True:
            chassis.drive(speed=1000, turn_rate=0)


if selected == "S":
    selected2 = hub_menu("D","W", "C","P")


    if selected2 == "D":
        hub.light.animate([Color.MAGENTA,Color(h=355, s=90, v=43)],interval=200)
        onboard_diagnosis()


    if selected2 == "P":
        hub.light.animate([Color.CYAN,Color.VIOLET],interval=200)
        chack_button_pressed()
   
    if selected2 == "C":
        color_on()


    if selected2 == "W":
        pressed = []
        while not any(pressed):
            pressed = hub.buttons.pressed()
            wait(10)


        hub.display.icon(Icon.CIRCLE)


        while any(hub.buttons.pressed()):
            wait(10)


        if Button.LEFT in pressed:
            we_won()
        elif Button.RIGHT in pressed:
            we_won()
        elif Button.BLUETOOTH in pressed:
            shubi_dubi()

