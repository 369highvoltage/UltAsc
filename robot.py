from wpilib import run, Joystick, SmartDashboard, CameraServer, SendableChooser
from utilities import truncate_float, normalize_range
from AsyncRobot import AsyncRobot
from CommandGroup import CommandGroup
from Command import Command, InstantCommand
from robot_map import RobotMap
from components.DriverComponent import DriverComponent
from components.DriverComponent.DriveCommands import DriveByTime, DriveByDistance, Turn, curve_drive, toggle_gear
from components.LifterComponent.LifterCommands import move_lifter, MoveUp, MoveDown, move_down_instant, move_up_instant, Reset, MoveToPosition, move_to_position_instant, lock_carriage_move_elevator
from components.GripperComponent.GripperCommands import move_left_right, toggle_spread, SpitFast, LiftTo, Toggle, close, spread, SuckFast
from components.ShooterComponent.ShooterCommands import Shoot
from autonomous.switch_scale import switch_scale, drive_straight
from components.ClimbComponent.ClimbCommands import climb, stop


class UltimateAscent(AsyncRobot):
    def __init__(self):
        super().__init__()

    # Create motors and stuff here
    def robotInit(self):
        self.driver = Joystick(0)
        CameraServer.launch('vision.py:main')

    def robotPeriodic(self):
        pass

    def autonomousInit(self):
        pass

    def autonomousPeriodic(self):
        pass

    def teleopInit(self):
        pass
    
    def teleopPeriodic(self):
        # Driving
        linear = -self.driver.getRawAxis(RobotMap.left_y)
        angular = self.driver.getRawAxis(RobotMap.right_x)
        RobotMap.driver_component.set_curve(linear, angular)

        # Square to toggle gear
        if self.driver.getRawButtonPressed(RobotMap.square):
            RobotMap.driver_component.toggle_gear()
        
        # Shooting (R2)
        launch_speed = -self.driver.getRawAxis(RobotMap.r_2)
        RobotMap.shooter_component.shoot(launch_speed)

        # X to fire
        if self.driver.getRawButtonPressed(RobotMap.x):
            self.start_command(Shoot())

        # Circle to toggle height
        if self.driver.getRawButtonPressed(RobotMap.circle):
            RobotMap.shooter_component.toggle_lifter()

if __name__ == '__main__':
    print("hello world")
    run(UltimateAscent)
