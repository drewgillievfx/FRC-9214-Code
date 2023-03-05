""""
----------------------------------------------------------------------------
Copyright (c) 2017-2018 FIRST. All Rights Reserved.
Open Source Software - may be modified and shared by FRC teams. The code
must be accompanied by the FIRST BSD license file in the root directory of
the project.
----------------------------------------------------------------------------

SPARK MAX controllers are intialized over CAN by constructing a
CANSparkMax object

The CAN ID, which can be configured using the SPARK MAX Client, is passed
as the first parameter

The motor type is passed as the second parameter.
Motor type can either be:
  rev.CANSparkMax.MotorType.kBrushless  ###################################
  rev.CANSparkMax.MotorType.kBrushed  #####################################

The example below initializes four brushless motors with CAN IDs
1, 2, 3, 4. Change these parameters to match your setup

self.cs = wpilib.CameraServer.getInstance()
self.cs.startAutomaticCapture(name="Camera", device="USB Camera 0")

"""
import rev
import wpilib
from wpilib.drive import DifferentialDrive



class Robot(wpilib.TimedRobot):
    # Joystick sensitivity.
    SENSITIVITY = 0.5
    # Drive train differential adjustment
    DIFFERENTIAL = 0.1
    # Speed setting. We found that 70% works best
    SPEED = 0.7

    def robotInit(self):
        wpilib.CameraServer.launch("vision.py:main")

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
        

        # Passing in the lead motors into DifferentialDrive allows any
        # commmands sent to the lead motors to be sent to the follower motors.
        self.driveTrain = DifferentialDrive(self.leftLeadMotor, self.rightLeadMotor)
        self.joystick = wpilib.Joystick(0)
        self.direction = -1

        # Setting up the joysticks.
        self._left_joystick = self.joystick.getRawAxis(1)
        self._right_joystick = self.joystick.getRawAxis(5)

        """
        The RestoreFactoryDefaults method can be used to reset the
        configuration parameters in the SPARK MAX to their factory default
        state. If no argument is passed, these parameters will not persist
        between power cycles 
        """
        # self.leftLeadMotor.restoreFactoryDefaults()
        # self.rightLeadMotor.restoreFactoryDefaults()
        # self.leftFollowMotor.restoreFactoryDefaults()
        # self.rightFollowMotor.restoreFactoryDefaults()

        """
        In CAN mode, one SPARK MAX can be configured to follow another. This
        is done by calling the follow() method on the SPARK MAX you want to
        configure as a follower, and by passing as a parameter the SPARK MAX
        you want to configure as a leader.
        """
        
        """
        This is shown in the example below, where one motor on each side of
        our drive train is configured to follow a lead motor.
        """
        self._left_follow_motor.follow(self._left_lead_motor)
        self._right_follow_motor.follow(self._right_lead_motor)
    
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
    
    # Drive Side.
    @property
    def left_drive_side(self):
        return self._left_drive_side
    @property
    def right_drive_side(self):
        return self._right_drive_side
    
    # Joysticks.
    @property
    def left_joystick(self):
        return self._left_joystick
    @property
    def right_joystick(self):
        return self._right_joystick
    
    ##########################################################################
    """ AUTO. """
    """
    AUTO 1:
        Drive forward for 2 seconds
        Stop for 2 seconds
        
    AUTO 2:
    AUTO 3:
    """
    
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

    ##########################################################################
    # TELEOP

    def teleopPeriodic(self):
        # Drive with arcade style
        """
        Buttons on controller on right side.
        ----------------------------------------------------------------------
        A button: self.joystick.getRawButton(1)
        B button: self.joystick.getRawButton(2)
        X button: self.joystick.getRawButton(3)
        Y button: self.joystick.getRawButton(4)

        LB button: self.joystick.getRawButton(5)
        RB button: self.joystick.getRawButton(6)
        ----------------------------------------------------------------------

        Joysticks
        ----------------------------------------------------------------------
        Left Joystick
        left/right --  self.joystick.getRawAxis(0)
        up/down --     self.joystick.getRawAxis(1)

        Right Joystick
        left/right -- self.joystick.getRawAxis(4)
        up/down --    self.joystick.getRawAxis(5)
        ----------------------------------------------------------------------

        Triggers
        ----------------------------------------------------------------------
        LT -- self.joystick.getRawAxis(2)
        RT -- self.joystick.getRawAxis(3)
        ----------------------------------------------------------------------
        """
        
        if  self.LB_Button:
            self.SPEED = 0
        elif  self.RB_Button:
            self.SPEED = 1
        
        else:
            self.SPEED = 0.7
        # self.speed = self.joystick.getRawAxis(3)
        # print(self.speed)


        # self.driveTrain.arcadeDrive(self.speed*self.joystick.getY(), self.speed*self.joystick.getX())

        if self.Y_Button:
            self.direction = -1*self.direction

        # drive forward
        elif self.direction == 1: 
            self.driveTrain.tankDrive(self.speed*self._left_joystick, self.speed*self._right_follow_motor)
        
        # drive backwards
        elif self.direction == -1: 
            self.driveTrain.tankDrive(-1*self.speed*self._right_follow_motor, -1*self.speed*self._left_joystick)
        
if __name__ == "__main__":
    wpilib.run(Robot)