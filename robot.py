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
from wpilib.drive import DifferentialDrive

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
class Robot(wpilib.TimedRobot):
    # Joystick sensitivity.
    SENSITIVITY = 0.5
    # Drive train differential adjustment
    DIFFERENTIAL = 0.1

 

    def robotInit(self):
        # Grabbing Left Motors. LLLLLLLLLLLLLLLLLLLLLLLLLLLLL
        self._left_lead_motor = rev.CANSparkMax(1,rev.CANSparkMax.MotorType.kBrushed)
        self._left_follow_motor = rev.CANSparkMax(2, rev.CANSparkMax.MotorType.kBrushed)

        self._left_lead_motor.setInverted(False)
        self._left_follow_motor.setInverted(False)
        
        # Grabbing Right Motors. RRRRRRRRRRRRRRRRRRRRRRRRRRRRR
        self._right_lead_motor = rev.CANSparkMax(3, rev.CANSparkMax.MotorType.kBrushed)
        self._right_follow_motor = rev.CANSparkMax(4, rev.CANSparkMax.MotorType.kBrushed)
        
        self._right_lead_motor.setInverted(True)
        self._right_follow_motor.setInverted(True) 
    
        # Setting up the motor controllers.
        self._left_drive_side = wpilib.MotorControllerGroup(
            self._left_lead_motor, self._left_follow_motor)
        
        self._right_drive_side = wpilib.MotorControllerGroup(
            self._right_lead_motor, self._right_follow_motor)

        # Setting up the joysticks.
        self._left_joystick = wpilib.Joystick(0)
        self._right_joystick = wpilib.Joystick(1)

        # Setting up a differential drive.
        self.drive_train = DifferentialDrive(self.left_drive_side,
                                             self.right_drive_side)
        self.drive_train.setExpiration(self.DIFFERENTIAL)

    # Drive Side.
    @property
    def left_drive_side(self):
        return self._left_drive_side
    @property
    def right_drive_side(self):
        return self._right_drive_side
    
    # Motors.
    @property
    def left_lead_motor(self):
        return self._left_lead_motor
    @property
    def left_follow_motor(self):
        return self._left_follow_motor
    @property
    def right_lead_motor(self):
        return self._right_lead_motor
    @property
    def right_follow_motor(self):
        return self._right_follow_motor
    
    # Joysticks.
    @property
    def left_joystick(self):
        return self._left_joystick
    @property
    def right_joystick(self):
        return self._right_joystick
    
    def spin(self, direction, speed: float):
        """ Spin is created for auto mode, to make changes more intuitive. """
        if direction == 'left':
            self.left_drive_side.set(speed)  # value is speed of gearbox
            self.right_drive_side.set(-speed)  # value is speed of gearbox
        elif direction == 'right':
            self.left_drive_side.set(-speed)  # value is speed of gearbox
            self.right_drive_side.set(speed)  # value is speed of gearbox
        else:
            self.left_drive_side.set(0.0)  # value is speed of gearbox
            self.right_drive_side.set(0.0)  # value is speed of gearbox

    def brake(self):
        """ Brake is created for auto mode, to make changes more intuitive. """
        self.left_drive_side.set(0.0)  # value is speed of gearbox
        self.right_drive_side.set(0.0)  # value is speed of gearbox

    def autonomousInit(self):
        """ This function is run once at the beginning of the match. """
        self.timer = wpilib.Timer()
        self.timer.start()
 
    def autonomousPeriodic(self):
        # Drive forward for 2 seconds.
        if self.timer.get() < 2.0:
            self.left_drive_side.set(0.5)  # value is speed of gearbox
            self.right_drive_side.set(0.5)  # value is speed of gearbox

        # Stop for 2 seconds.
        elif self.timer.get() < 4.0:
            self.brake()

        # Spin  for 2 seconds.
        elif self.timer.get() < 6.0:
            self.spin('left', 0.5)

        # Stop for 2 seconds.
        elif self.timer.get() < 8.0:
            self.brake()

        else:
            self.left_drive_side.set(0.0)  # value is speed of gearbox
            self.right_drive_side.set(0.0)  # value is speed of gearbox

    def teleopPeriodic(self):
        """
        Motor speed is determined by the joystick input values
        and the sensitivity set at beginning of class. 
        """
        left_speed = self._left_joystick.getY() * self.SENSITIVITY
        right_speed = self._right_joystick.getY() * self.SENSITIVITY

        # Now set the motor speed to the joystick values.
        self._left_drive_side.set(left_speed)
        self._right_drive_side.set(right_speed)

##############################################################################
##############################################################################
# main
if __name__ == '__main__':   
    status_check(0)  # Set status to 0 for at home || and 1 for at event
    print(F'\nStarting Robot\n')
    wpilib.run(Robot())
    print(F'\nRobot Ready for Shutdown\n')
