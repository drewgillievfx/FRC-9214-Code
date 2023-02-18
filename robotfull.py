#!/usr/bin/env python3
# """
#     This is a good foundation to build your robot code on
# """

# import rev
import wpilib
import wpilib.drive


class MyRobot(wpilib.TimedRobot):

    def robotInit(self):
        # """
        # This function is called upon program startup and
        # should be used for any initialization code.
        # """
        # self.cs = wpilib.CameraServer.getInstance()
        # self.cs.startAutomaticCapture(name="Camera", device="USB Camera 0")

        # self.left_motor = rev.CANSparkMax(1,rev.CANSparkMaxLowLevel.MotorType.kBrushless)
        # self.right_motor = rev.CANSparkMax(2,rev.CANSparkMaxLowLevel.MotorType.kBrushless)
        # self.drive = wpilib.drive.DifferentialDrive(self.left_motor, self.right_motor)


        # We might want to use this....
        # https://robotpy.readthedocs.io/en/latest/guide/anatomy.html#robot-drivetrain-control
        
        self.frontRight = wpilib.Spark(1)
        self.rearRight = wpilib.Spark(2)
        self.right = wpilib.SpeedControllerGroup(self.frontRight, self.rearRight)
        
        self.frontLeft = wpilib.Spark(3)
        self.rearLeft = wpilib.Spark(4)
        self.left = wpilib.SpeedControllerGroup(self.frontLeft, self.rearLeft)


        self.drive = wpilib.drive.DifferentialDrive(self.left, self.right)


        
        self.stick = wpilib.Joystick(1)
        self.timer = wpilib.Timer()

    def autonomousInit(self):
        # """This function is run once each time the robot enters autonomous mode."""
        self.timer.reset()
        self.timer.start()

    def autonomousPeriodic(self):
        # """This function is called periodically during autonomous."""

        # Drive for two seconds
        if self.timer.get() < 2.0:
            self.drive.arcadeDrive(-0.5, 0)  # Drive forwards at half speed
        else:
            self.drive.arcadeDrive(0, 0)  # Stop robot

    def teleopPeriodic(self):
        # """This function is called periodically during operator control."""
        # speed = 0.5  # default speed
        # if self.stick.getRawButton(1):  # check if the A button is pressed
        #     speed = 1  # increase speed to 100%
        # if self.stick.getRawButton(2): # check if the X button is pressed
        #     self.turn_robot(90) # call the turn_robot function
        # if self.stick.getRawButton(3): # check if the B button is pressed
        #     self.turn_robot(-90) # call the turn_robot function with a negative angle

        self.drive.arcadeDrive(self.stick.getY(), self.stick.getX())


    # def turn_robot(self, angle):
    #     self.gyro.reset() #reset the gyro
    #     while abs(self.gyro.getAngle()) < angle: # while the robot hasn't turned the desired angle
    #         self.drive.arcadeDrive(0, 1) # turn the robot to the left at full speed


if __name__ == "__main__":
    wpilib.run(MyRobot)