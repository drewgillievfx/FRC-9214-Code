#!/usr/bin/env python3

import wpilib
import ctre
import rev


class MyRobot(wpilib.TimedRobot):
    """
    This is a short sample program demonstrating how to use the basic throttle
    mode of the TalonSRX
    """

    def robotInit(self):
        # Setup Joystick
        self.Joystick = wpilib.Joystick(0)
        

        self.LeftFrontMotor = ctre.WPI_TalonSRX(1)
        self.LeftRearMotor = ctre.WPI_TalonSRX(2)
        self.LeftRearMotor.follow(self.LeftFrontMotor)

        self.RightFrontMotor = ctre.WPI_TalonSRX(3)
        self.RightRearMotor = ctre.WPI_TalonSRX(4)
        self.RightRearMotor.follow(self.RightFrontMotor)

        self.JackShaftMotor = rev.CANSparkMax(6,rev.CANSparkMax.MotorType.kBrushless)
        self.encoder = self.JackShaftMotor.getEncoder()
        # self.controller = wpilib.PIDController(1, 0, 0, self.encoder, self.JackShaftMotor)

        self.IntakeMotor = rev.CANSparkMax(7,rev.CANSparkMax.MotorType.kBrushless)
        

    def disabledPeriodic(self):
        self.LeftFrontMotor.disable()
        self.LeftRearMotor.disable()
        self.RightFrontMotor.disable()
        self.RightRearMotor.disable()
        self.IntakeMotor.disable()
        self.JackShaftMotor.disable()

    def teleopPeriodic(self):

        self.LEFT_THUMB_LEFTRIGHT = self.Joystick.getRawAxis(0)
        self.LEFT_THUMB_UPDOWN = self.Joystick.getRawAxis(1)
        self.RIGHT_THUMB_LEFTRIGHT = self.Joystick.getRawAxis(4)
        self.RIGHT_THUMB_UPDOWN = self.Joystick.getRawAxis(5)

        self.LEFT_TRIGGER=self.Joystick.getRawAxis(2)
        self.RIGHT_TRIGGER=self.Joystick.getRawAxis(3)

        self.A_Button=self.Joystick.getRawButton(1)
        self.B_Button=self.Joystick.getRawButton(2)
        self.X_Button=self.Joystick.getRawButton(3)
        self.Y_Button=self.Joystick.getRawButton(4)
        self.LB_Button=self.Joystick.getRawButton(5)
        self.RB_Button=self.Joystick.getRawButton(6)



        # Set the motor's output to half power.
        # This takes a number from -1 (100% speed in reverse) to +1 (100%
        # speed going forward)
        # if self.A_Button:
        self.Speed=0.5
        self.LeftFrontMotor.set(-1*self.Speed*self.LEFT_THUMB_UPDOWN)
        self.RightFrontMotor.set(self.Speed*self.RIGHT_THUMB_UPDOWN)

        # if self.RIGHT_TRIGGER > 0:
        #     self.IntakeMotor.set(self.Speed*self.RIGHT_TRIGGER)
        # if self.LEFT_TRIGGER > 0:
        #     self.IntakeMotor.set(-1*self.Speed*self.LEFT_TRIGGER)

        # Move the jackshaft to the up position:
        if self.Y_Button:
            current_position = self.encoder.getPosition() # get current position of motor
            print("Current position:", current_position)
            self.encoder.setPosition()
            
        if self.RIGHT_TRIGGER > 0:
            self.JackShaftMotor.set(self.Speed*self.RIGHT_TRIGGER)
        if self.LEFT_TRIGGER > 0:
            self.JackShaftMotor.set(-1*self.Speed*self.LEFT_TRIGGER)
        

        # if self.B_Button:
        #     self.LeftFrontMotor.set(1.0)
        # if self.Y_Button:
        #     self.LeftFrontMotor.set(0)
            


if __name__ == "__main__":
    wpilib.run(MyRobot)