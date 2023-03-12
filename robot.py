#!/usr/bin/env python3

import wpilib
import ctre
import rev
from wpilib import SmartDashboard


class MyRobot(wpilib.TimedRobot):
    """
    This is a short sample program demonstrating how to use the basic throttle
    mode of the TalonSRX
    """

    def robotInit(self):
        
        self.ARM_EXTENDED_ENCODER=-18
        self.ARM_FULLY_RETRACTED_ENCODER=12
        self.ARM_HALF_RETRACTED_ENCODER=6
        self.ARM_POSITION = "Half"
        self.INTAKE_STATE = "Stopped"
        
        
        self.SMARTArmRotation = SmartDashboard.putNumber("Arm Rotation", 0)
        self.SMARTArmRotation = SmartDashboard.putString("Arm Position", self.ARM_POSITION)
        
        self.DriveJoystick = wpilib.Joystick(0)
        self.ArmJoystick = wpilib.Joystick(1)

        self.LeftFrontMotor = ctre.WPI_TalonSRX(1)
        self.LeftRearMotor = ctre.WPI_TalonSRX(2)
        self.LeftRearMotor.follow(self.LeftFrontMotor)

        self.RightFrontMotor = ctre.WPI_TalonSRX(3)
        self.RightRearMotor = ctre.WPI_TalonSRX(4)
        self.RightRearMotor.follow(self.RightFrontMotor)

        self.JackShaftMotor = rev.CANSparkMax(6,rev.CANSparkMax.MotorType.kBrushless)
        self.JackShaftMotor.setIdleMode(rev.CANSparkMax.IdleMode.kBrake)
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
        self.DriveJoystickVariable()
        self.DriveMotors()

        self.ArmJoystickVariable()
        self.ArmMotors()

        self.IntakeMotors()
            
        
    def DriveJoystickVariable(self):
        self.DRIVE_LEFT_THUMB_LEFTRIGHT = self.DriveJoystick.getRawAxis(0)
        self.DRIVE_LEFT_THUMB_UPDOWN = self.DriveJoystick.getRawAxis(1)
        self.DRIVE_RIGHT_THUMB_LEFTRIGHT = self.DriveJoystick.getRawAxis(4)
        self.DRIVE_RIGHT_THUMB_UPDOWN = self.DriveJoystick.getRawAxis(5)

        self.DRIVE_LEFT_TRIGGER=self.DriveJoystick.getRawAxis(2)
        self.DRIVE_RIGHT_TRIGGER=self.DriveJoystick.getRawAxis(3)

        self.DRIVE_A_Button=self.DriveJoystick.getRawButton(1)
        self.DRIVE_B_Button=self.DriveJoystick.getRawButton(2)
        self.DRIVE_X_Button=self.DriveJoystick.getRawButton(3)
        self.DRIVE_Y_Button=self.DriveJoystick.getRawButton(4)
        self.DRIVE_LB_Button=self.DriveJoystick.getRawButton(5)
        self.DRIVE_RB_Button=self.DriveJoystick.getRawButton(6)

    
        
    def DriveMotors(self):
        # Set the motor's output to half power.
        # This takes a number from -1 (100% speed in reverse) to +1 (100%
        # speed going forward)
        self.DriveSpeed=1.0

        # High Speed
        # Set the motor's output to FULL power.
        if self.DRIVE_RB_Button:
            self.DriveSpeed=0.7

        # Slow speed
        # Set the motor's output to 1/3 power.
        if self.DRIVE_RIGHT_TRIGGER>0:
            self.DriveSpeed=0.5

        # STOP button
        # Set the motor's output to ZERO power.
        if self.DRIVE_LB_Button:
            self.DriveSpeed=0
        self.LeftFrontMotor.set(-1*self.DriveSpeed*self.DRIVE_LEFT_THUMB_UPDOWN)
        self.LeftRearMotor.set(-1*self.DriveSpeed*self.DRIVE_LEFT_THUMB_UPDOWN)
        self.RightFrontMotor.set(self.DriveSpeed*self.DRIVE_RIGHT_THUMB_UPDOWN)
        self.RightRearMotor.set(self.DriveSpeed*self.DRIVE_RIGHT_THUMB_UPDOWN)

    def ArmJoystickVariable(self):
        self.ARM_LEFT_THUMB_LEFTRIGHT = self.ArmJoystick.getRawAxis(0)
        self.ARM_LEFT_THUMB_UPDOWN = self.ArmJoystick.getRawAxis(1)
        self.ARM_RIGHT_THUMB_LEFTRIGHT = self.ArmJoystick.getRawAxis(4)
        self.ARM_RIGHT_THUMB_UPDOWN = self.ArmJoystick.getRawAxis(5)

        self.ARM_LEFT_TRIGGER=self.ArmJoystick.getRawAxis(2)
        self.ARM_RIGHT_TRIGGER=self.ArmJoystick.getRawAxis(3)

        self.ARM_A_Button=self.ArmJoystick.getRawButton(1)
        self.ARM_B_Button=self.ArmJoystick.getRawButton(2)
        self.ARM_X_Button=self.ArmJoystick.getRawButton(3)
        self.ARM_Y_Button=self.ArmJoystick.getRawButton(4)
        self.ARM_LB_Button=self.ArmJoystick.getRawButton(5)
        self.ARM_RB_Button=self.ArmJoystick.getRawButton(6)

    def ArmMotors(self):
        self.ArmSpeed=0.2
            

        if self.ARM_Y_Button:
            self.ARM_POSITION = "Extended"
        
        elif self.ARM_B_Button:
            self.ARM_POSITION = "Half"

        elif self.ARM_A_Button:
            self.ARM_POSITION = "Retract"

        
        elif self.ARM_X_Button:
            self.ARM_POSITION = ""
        
        Jackshaft_position = self.encoder.getPosition()
        self.SMARTArmRotation = SmartDashboard.putNumber("Arm Rotation", Jackshaft_position)
        self.SMARTArmRotation = SmartDashboard.putString("Arm Position", self.ARM_POSITION)
        SmartDashboard.
        
        
        

            
        if self.ARM_POSITION=="Extended":
            if Jackshaft_position > self.ARM_EXTENDED_ENCODER:
                self.JackShaftMotor.set(-1*self.ArmSpeed)
            else:
                self.JackShaftMotor.set(0)
        
        elif self.ARM_POSITION=="Half":
            if Jackshaft_position < self.ARM_HALF_RETRACTED_ENCODER:
                self.JackShaftMotor.set(-1*self.ArmSpeed)
            elif Jackshaft_position > self.ARM_HALF_RETRACTED_ENCODER:
                self.JackShaftMotor.set(self.ArmSpeed)
            else:
                self.JackShaftMotor.set(0)

        elif self.ARM_POSITION=="Retract":
            if Jackshaft_position < self.ARM_FULLY_RETRACTED_ENCODER:
                self.JackShaftMotor.set(self.ArmSpeed)
            else:
                self.JackShaftMotor.set(0)

         

        
        
        
        if self.ARM_LB_Button:
            self.JackShaftMotor.set(-1*self.ArmSpeed*self.ARM_RIGHT_THUMB_UPDOWN)
        else:
            self.JackShaftMotor.set(0)

    def IntakeMotors(self):
        if self.ARM_LEFT_TRIGGER:
            self.INTAKE_STATE = "Intake"
        
        elif self.ARM_RIGHT_TRIGGER:
            self.INTAKE_STATE = "Release"
        
        elif self.ARM_RB_Button:
            self.INTAKE_STATE = "Stopped"
       

        self.IntakeSpeed=0.3

        Intake_Current=self.IntakeMotor.getOutputCurrent()
        self.SMARTArmRotation = SmartDashboard.putNumber("Intake Current", Intake_Current)
        self.SMARTArmRotation = SmartDashboard.putString("Intake State", self.INTAKE_STATE)
            
        # if Intake_Current > 5:
        #     self.IntakeMotor.set(0)
        # el
        
        
        if self.INTAKE_STATE=="Intake":
            self.IntakeMotor.set(self.IntakeSpeed)
        elif self.INTAKE_STATE=="Release":
            self.IntakeMotor.set(-1*self.IntakeSpeed)
        else:
            self.IntakeMotor.set(0)
       
if __name__ == "__main__":
    wpilib.run(MyRobot)


    



