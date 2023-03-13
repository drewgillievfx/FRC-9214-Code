#!/usr/bin/env python3

import wpilib
import ctre
import rev
# import neopixel
# import board


class MyRobot(wpilib.TimedRobot):
    """
    This is a short sample program demonstrating how to use the basic throttle
    mode of the TalonSRX
    """

    def robotInit(self):
        # Setup Joystick
        self.DriverJoystick = wpilib.Joystick(0)
        self.OperatorJoystick = wpilib.Joystick(1)

        self.LeftFrontMotor = ctre.WPI_TalonSRX(1)
        self.LeftRearMotor = ctre.WPI_TalonSRX(2)

        self.RightFrontMotor = ctre.WPI_TalonSRX(3)
        self.RightRearMotor = ctre.WPI_TalonSRX(4)

        self.JackShaftMotor = rev.CANSparkMax(6,rev.CANSparkMax.MotorType.kBrushless)
        self.JackShaftMotor.setInverted(True)
        self.JackShaftMotor.setIdleMode(rev.CANSparkMax.IdleMode.kBrake)

        self.ArmEncoder = self.JackShaftMotor.getEncoder()
        self.ArmEncoder.setPosition(0)

        self.IntakeMotor = rev.CANSparkMax(7,rev.CANSparkMax.MotorType.kBrushless)

        self.wantedArmPosition = 0
        self.armRunningToPosition = False

        # Constants
        self.MaxDriveSpeed=0.75
        self.MaxArmSpeed=0.5
        self.UpperArm = 75
        self.LowerArm = 60
        self.armHome = 2

        #Auto inits
        self.AutoTimer = wpilib.Timer()

        # pixel_pin = board.D1 # change this to match the pin you're using
        # num_pixels = 60 # change this to match the number of LEDs in your strip
        # ORDER = neopixel.GRB # change this to match your LED strip's color order
        # self.pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=1.0, auto_write=False, pixel_order=ORDER)


    def setDrives(self, leftSpeed: float, rightSpeed: float):
        self.LeftFrontMotor.set(-leftSpeed)
        self.LeftRearMotor.set(-leftSpeed)
        self.RightFrontMotor.set(rightSpeed)
        self.RightRearMotor.set(rightSpeed)

    # returns if arms are moving for position
    def setArmPosition(self, position: int):
        offset = 1
        currentPosition = self.ArmEncoder.getPosition()
        print("Current position:", currentPosition, " Wanted: ", position)
        if(currentPosition > position + offset):
            self.JackShaftMotor.set(-0.5)
        elif(currentPosition < position - offset):
            self.JackShaftMotor.set(0.5)
        else:
            if (currentPosition < 10):
                self.JackShaftMotor.set(-0.01)
            else:
                self.JackShaftMotor.set(0.03)
            self.armRunningToPosition = False

    def autonomousInit(self):
        self.AutoTimer.reset()
        self.AutoTimer.start()

    def autonomousPeriodic(self):
        if(self.AutoTimer.get() < 0.5):
            self.setDrives(0.5, 0.5)
        elif(self.AutoTimer.get() < 5):
            self.setDrives(-0.4, -0.4)
        else:
            self.setDrives(0, 0)
        

    def disabledPeriodic(self):
        self.LeftFrontMotor.disable()
        self.LeftRearMotor.disable()
        self.RightFrontMotor.disable()
        self.RightRearMotor.disable()
        self.IntakeMotor.disable()
        self.JackShaftMotor.disable()

    def teleopPeriodic(self):

        self.LEFT_THUMB_LEFTRIGHT = self.DriverJoystick.getRawAxis(0)
        self.LEFT_THUMB_UPDOWN = self.DriverJoystick.getRawAxis(1)
        self.RIGHT_THUMB_LEFTRIGHT = self.DriverJoystick.getRawAxis(4)
        self.RIGHT_THUMB_UPDOWN = self.DriverJoystick.getRawAxis(5)
        self.DRIVEX_Button=self.DriverJoystick.getRawButton(3)
        self.DRIVEY_Button=self.DriverJoystick.getRawButton(4)

        self.LEFT_TRIGGER=self.OperatorJoystick.getRawAxis(2)
        self.RIGHT_TRIGGER=self.OperatorJoystick.getRawAxis(3)

        self.Acquire =self.OperatorJoystick.getRawAxis(1)
        self.A_Button=self.OperatorJoystick.getRawButton(1)
        self.B_Button=self.OperatorJoystick.getRawButton(2)
        self.X_Button=self.OperatorJoystick.getRawButton(3)
        self.Y_Button=self.OperatorJoystick.getRawButton(4)
        self.LB_Button=self.OperatorJoystick.getRawButton(5)
        self.RB_Button=self.OperatorJoystick.getRawButton(6)

        #Driver
        rightSpeed = self.MaxDriveSpeed*self.RIGHT_THUMB_UPDOWN
        leftSpeed = self.MaxDriveSpeed*self.LEFT_THUMB_UPDOWN
        self.setDrives(leftSpeed, rightSpeed)

        # if(self.DRIVEX_Button):
        #     self.setGamePiece("cube")
        # elif(self.DRIVEY_Button):
        #     self.setGamePiece("cone")
        # else:
        #     self.setGamePiece("none")


        #Operator
        if(self.A_Button):
            self.wantedArmPosition = self.armHome
            self.armRunningToPosition = True
        elif(self.B_Button):
            self.wantedArmPosition = self.LowerArm
            self.armRunningToPosition = True
        elif(self.Y_Button):
            self.wantedArmPosition = self.UpperArm 
            self.armRunningToPosition = True

        # Move the jackshaft to the up position:
        if self.X_Button:
            self.armRunningToPosition = False
        
        if(self.armRunningToPosition):
            self.setArmPosition(self.wantedArmPosition)
        else:
            if self.RIGHT_TRIGGER > 0.05:
                self.JackShaftMotor.set(self.MaxArmSpeed*self.RIGHT_TRIGGER)
            if self.LEFT_TRIGGER > 0.05:
                self.JackShaftMotor.set(-1*self.MaxArmSpeed*self.LEFT_TRIGGER)
    # def setGamePiece(self,gamePiece):
    #     if gamePiece == "cube":
    #         self.pixels.fill((255, 0, 255))
    #         self.pixels.show()
    #     elif gamePiece == "cone":
    #         self.pixels.fill((255, 255, 0))
    #         self.pixels.show()
    #     elif gamePiece == "none":
    #         self.pixels.fill((0, 0, 0))
    #         self.pixels.show()

    #     if (self.Acquire > 0.1):
    #         self.IntakeMotor.set(0.2)
    #     elif(self.Acquire < -0.1):
    #         self.IntakeMotor.set(-0.5)
    #     else:
    #         self.IntakeMotor.set(0)

if __name__ == "__main__":
    wpilib.run(MyRobot)