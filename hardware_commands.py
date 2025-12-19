from XRPLib.differential_drive import DifferentialDrive
from XRPLib.reflectance import Reflectance
from XRPLib.servo import Servo
import time


drive = DifferentialDrive.get_default_differential_drive()
reflect = Reflectance.get_default_reflectance()
gripper = Servo.get_default_servo(1)

SPEED = 0.35
TURN_GAIN = 0.6
LINE_THRESHOLD = 0.3

def follow_line_step(): #intially built on the XRP code blockly provided and showed in the Digikey tutorial
    """Executes one step of PID-like line following """ 
    left = reflect.get_left()
    right = reflect.get_right()
    turn_effort = (left - right) * TURN_GAIN
    drive.arcade(SPEED, max(-1.0, min(1.0, turn_effort)))

def execute_pickup():
    """Automated sequence for bucket pickup """
    drive.stop() #stops the robot in front of the bucket
    drive.turn(180, 0.6) #turns the robot 180 degrees where it is supposedly facing the bucket now
    time.sleep(1)#stops for 1 second to make sure it is aligned
    gripper.set_angle(60) # sets the servo to a 60 degrees angle - this was the defult I chose but often the gripper fell so I had to rearrange it by eye making the angle change often
    drive.straight(-30, 0.5) # back up to target about 30 cm to make sure that it has reached the bucket
    time.sleep(1)# stops for 1 second
    gripper.set_angle(10) # the sevo brings the gripper up to pull up the bucket from the ground
    time.sleep(1) # stops for 1 second again
    drive.straight(10, 0.5) # drives for 10 cm forward
    drive.stop() # stops

def check_line_end():
    """Detects if robot has reached the end of the course]"""
    return reflect.get_left() < 0.7 and reflect.get_right() > 0.7 # after checking the sensor myself I have seen that both values go to a value of approx 0.68 once it leaves the line therefore setting the condition for the robot to identfy itself off the line to this value
