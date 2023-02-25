"""
    Start Date: 20230218
    Version: 1.0
    Started by: Drew Gillie

    At event - radio must be configured at the kiosk

    MATCH start 0:15
        (for AUTO) “Cavalry Charge”
    AUTO ends 0:00
        (for AUTO) “Buzzer”
    TELEOP begins 2:15
        “3 Bells”
    ENDGAME begins 0:30
        “Train Whistle”
    MATCH end 0:00
        “Buzzer”
    MATCH stopped
        “Foghorn
"""

# imports
""" Import all necessary libraries and other scripts into this main file. """
import rev
import wpilib
import wpilib.drive
from robot_class import Robot

##############################################################################
def status_check(status):
    
    if status == 0:
        mode = 'HOME'
        print(F'The Robot is in {mode} mode.')
    elif status == 1:
        mode = 'EVENT'
        print(F'The Robot is in {mode} mode.')
    else:
        print('The robot is in standby mode - there may be a \
            communication error.')
##############################################################################
##############################################################################
# main
if __name__ == '__main__':   
    status_check(0)  # Set status to 0 for at home || and 1 for at event
    print(F'\nStarting Robot\n')
    wpilib.run(robot_class.Robot())
    print(F'\nRobot Ready for Shutdown\n')
