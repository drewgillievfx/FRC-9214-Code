"""
The robot class is determined by the code in this script.
The goal is to create a class for the robot to set and access the
various parts of the electronics that control the robot.

Main functions of the robot are as follows:
    Drive system
        4 motors (2 per gearbox)
        6 wheels
    Arm Mechanism
"""
import wpilib

class MyRobot(wpilib.TimedRobot):
    # Joystick sensitivity.
    SENSITIVITY = 0.5

    def robotInit(self):
        # Setting up the motor controllers.
        self._left_drive_side = wpilib.SpeedControllerGroup(wpilib.Spark(3),
                                                            wpilib.Spark(4))
        self._right_drive_side = wpilib.SpeedControllerGroup(wpilib.Spark(1),
                                                             wpilib.Spark(2))

        # Setting up the joysticks.
        self._left_joystick = wpilib.Joystick(0)
        self._right_joystick = wpilib.Joystick(1)


    @property
    def left_drive_side(self):
        return self._left_drive_side
    @property
    def right_drive_side(self):
        return self._right_drive_side
    
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