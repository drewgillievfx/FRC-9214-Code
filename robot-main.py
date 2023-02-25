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
# import wpilib
# import wpilib.drive

##############################################################################
##############################################################################
# main
if __name__ == '__main__':   
    """ Set the status of the robot to be at home or at competition. """ 
    status = 'HOME'
    # status = 'EVENT'

    print(F'\nStarting Robot\n')

    """ 
    Run Robot Code Here.

    This will look something like

        if match at competition:
            wait for field signal
                run autonomous
            wait for field signal
                enable teleop
            wait for field signal
                disable robot
        elif practice at competition:
            switch
                test auto
                test teleop
        else:
            switch
                test auto
                test teleop
    """

    if status == 'HOME':
        print(F'The Robot is in {status} mode.')
    elif status == 'EVENT':
        print(F'The Robot is in {status} mode.')
        mode = 'AUTO'
        # robot.auto
        mode = 'TELEOP'
        #robot.telop

    else:
        print('The robot is in standby mode - there may be a \
              communication error.')

    # wpilib.run(MyRobot)
    print(F'\nRobot Ready for Shutdown\n')