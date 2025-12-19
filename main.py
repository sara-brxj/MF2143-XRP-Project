import hardware_commands as rc
import communication as comm
import time

# Define the States
STATE_FOLLOW_LINE = "FOLLOW"
STATE_PICKUP = "PICKUP"
STATE_WAIT_VOICE = "VOICE"
STATE_FINISH = "FINISH"

current_state = STATE_FOLLOW_LINE

print("=== Starting System ===")

while True:
    if current_state == STATE_FOLLOW_LINE:
        rc.follow_line_step()
        
        if comm.get_ml_signal() == "bucket":
            print("ML Detection: Bucket Found!")
            current_state = STATE_PICKUP
            
    elif current_state == STATE_PICKUP:
        rc.execute_pickup() 
        current_state = STATE_WAIT_VOICE
        
    elif current_state == STATE_WAIT_VOICE:
        command = comm.get_voice_command() 
        
        if command == "go":
            rc.drive.straight(20, 0.5)
            
        elif command == "left":
            rc.drive.turn(-90, 0.5) 
          
            
        elif command == "right":
            rc.drive.turn(90, 0.5) 
          
            
    elif current_state == STATE_FINISH:
        rc.follow_line_step()
        if rc.check_line_end():
            rc.drive.stop()
            print("Mission Accomplished!")
            break
 
