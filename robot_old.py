# ----------------------------------------------------------------------------
# Copyright (c) 2017-2018 FIRST. All Rights Reserved.
# Open Source Software - may be modified and shared by FRC teams. The code
# must be accompanied by the FIRST BSD license file in the root directory of
# the project.
# ----------------------------------------------------------------------------

import rev
import wpilib
from wpilib.drive import DifferentialDrive


class Robot(wpilib.TimedRobot):
    def robotInit(self):
        # SPARK MAX controllers are intialized over CAN by constructing a
        # CANSparkMax object
        #
        # The CAN ID, which can be configured using the SPARK MAX Client, is passed
        # as the first parameter
        #
        # The motor type is passed as the second parameter.
        # Motor type can either be:
        #   rev.CANSparkMax.MotorType.kBrushless
        #   rev.CANSparkMax.MotorType.kBrushed
        #
        # The example below initializes four brushless motors with CAN IDs
        # 1, 2, 3, 4. Change these parameters to match your setup

        # self.cs = wpilib.CameraServer.getInstance()
        # self.cs.startAutomaticCapture(name="Camera", device="USB Camera 0")

        # wpilib.CameraServer.launch()

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


        # print("axis",self.joystick.getRawAxis(5))

        # if  self.joystick.getRawButton(1):
        #     self.speed=1
        # else:
        #     self.speed=0.7
        self.speed = self.joystick.getRawAxis(3)
        print(self.speed)


        self.driveTrain.arcadeDrive(self.speed*self.joystick.getY(), self.speed*self.joystick.getX())

        # self.driveTrain.tankDrive(self.joystick.getRawAxis(0), self.joystick.getRawAxis(1))
        # self.driveTrain.tankDrive
if __name__ == "__main__":
    wpilib.run(Robot)