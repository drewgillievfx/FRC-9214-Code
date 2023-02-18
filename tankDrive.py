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

        wpilib.CameraServer.launch()

        self.frontLeftMotor  = rev.CANSparkMax(1,rev.CANSparkMax.MotorType.kBrushed)
        self.rearLeftMotor  = rev.CANSparkMax(2, rev.CANSparkMax.MotorType.kBrushed)


        self.frontRightMotor  = rev.CANSparkMax(3, rev.CANSparkMax.MotorType.kBrushed)
        self.rearRightMotor  = rev.CANSparkMax(4, rev.CANSparkMax.MotorType.kBrushed)

        # self.frontRightMotor.setInverted(False)
        # self.rearLeftMotor.setInverted(False)
        
        # self.frontRightMotor.setInverted(True)
        # self.rearRightMotor.setInverted(True)        

        
        self.left = wpilib.MotorControllerGroup(self.frontLeftMotor, self.rearLeftMotor)
        self.right = wpilib.MotorControllerGroup(
            self.frontRightMotor, self.rearRightMotor
        )

        self.myRobot = DifferentialDrive(self.left, self.right)
        self.myRobot.setExpiration(0.1)

        # joysticks 1 & 2 on the driver station
        self.leftStick = wpilib.Joystick(0)
        self.rightStick = wpilib.Joystick(1)

    def teleopInit(self):
        """Executed at the start of teleop mode"""
        self.myRobot.setSafetyEnabled(True)

    def teleopPeriodic(self):
        # Drive with arcade style

        self.speed=0.5


        self.myRobot.tankDrive(self.leftStick.getY() * -1, self.rightStick.getY() * -1)

        
if __name__ == "__main__":
    wpilib.run(Robot)