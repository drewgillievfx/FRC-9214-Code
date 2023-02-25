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

    def robotInit(self):
        wpilib.CameraServer.launch("vision.py:main")

        self.leftLeadMotor = rev.CANSparkMax(1,rev.CANSparkMax.MotorType.kBrushed)
        self.leftFollowMotor = rev.CANSparkMax(2, rev.CANSparkMax.MotorType.kBrushed)


        self.rightLeadMotor = rev.CANSparkMax(3, rev.CANSparkMax.MotorType.kBrushed)
        self.rightFollowMotor = rev.CANSparkMax(4, rev.CANSparkMax.MotorType.kBrushed)

        self.leftLeadMotor.setInverted(False)
        self.leftFollowMotor.setInverted(False)
        
        self.rightLeadMotor.setInverted(True)
        self.rightFollowMotor.setInverted(True)        

        

        # Passing in the lead motors into DifferentialDrive allows any
        # commmands sent to the lead motors to be sent to the follower motors.
        self.driveTrain = DifferentialDrive(self.leftLeadMotor, self.rightLeadMotor)
        self.joystick = wpilib.Joystick(0)
        self.direction=-1

        self.leftThumbJoyStick=self.joystick.getRawAxis(1)
        self.rightThumbJoyStick=self.joystick.getRawAxis(5)

        # The RestoreFactoryDefaults method can be used to reset the
        # configuration parameters in the SPARK MAX to their factory default
        # state. If no argument is passed, these parameters will not persist
        # between power cycles
        # self.leftLeadMotor.restoreFactoryDefaults()
        # self.rightLeadMotor.restoreFactoryDefaults()
        # self.leftFollowMotor.restoreFactoryDefaults()
        # self.rightFollowMotor.restoreFactoryDefaults()

        # In CAN mode, one SPARK MAX can be configured to follow another. This
        # is done by calling the follow() method on the SPARK MAX you want to
        # configure as a follower, and by passing as a parameter the SPARK MAX
        # you want to configure as a leader.
        #
        # This is shown in the example below, where one motor on each side of
        # our drive train is configured to follow a lead motor.
        self.leftFollowMotor.follow(self.leftLeadMotor)
        self.rightFollowMotor.follow(self.rightLeadMotor)

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
        # Drive with arcade style

        self.speed=0.7


        # A button: self.joystick.getRawButton(1)
        # B button: self.joystick.getRawButton(2)
        # X button: self.joystick.getRawButton(3)
        # Y button: self.joystick.getRawButton(4)
        # LB button: self.joystick.getRawButton(5)
        # RB button: self.joystick.getRawButton(6)

        # left/right on the left thumb joystick self.joystick.getRawAxis(0)
        # up/down on the left thumb joystick self.joystick.getRawAxis(1)
        # LT  self.joystick.getRawAxis(2)
        # RT  self.joystick.getRawAxis(3)
        # left/right on the right thumb joystick self.joystick.getRawAxis(4)
        # up/down on the right thumb joystick self.joystick.getRawAxis(5)

        self.Y_Button=self.joystick.getRawButton(4)
        self.LB_Button=self.joystick.getRawButton(5)
        self.RB_Button=self.joystick.getRawButton(6)
        self.leftThumbJoyStick=self.joystick.getRawAxis(1)
        self.rightThumbJoyStick=self.joystick.getRawAxis(5)

        
        

            

        if  self.LB_Button:
            self.speed=0
        elif  self.RB_Button:
            self.speed=1
        
        else:
            self.speed=0.7
        # self.speed = self.joystick.getRawAxis(3)
        # print(self.speed)


        # self.driveTrain.arcadeDrive(self.speed*self.joystick.getY(), self.speed*self.joystick.getX())



        if self.Y_Button:
            self.direction=-1*self.direction

            
        # drive forward
        elif self.direction==1: 
            self.driveTrain.tankDrive(self.speed*self.leftThumbJoyStick, self.speed*self.rightThumbJoyStick)
        
        # drive backwards
        elif self.direction==-1: 
            self.driveTrain.tankDrive(-1*self.speed*self.rightThumbJoyStick, -1*self.speed*self.leftThumbJoyStick)
        
##############################################################################
##############################################################################
# main
if __name__ == '__main__':   
    # status_check(0)  # Set status to 0 for at home || and 1 for at event
    print(F'\nStarting Robot\n')
    wpilib.run(Robot)
    print(F'\nRobot Ready for Shutdown\n')