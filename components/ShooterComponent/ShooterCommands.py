from robot_map import RobotMap
from Command import InstantCommand, Command
from wpilib.timer import Timer
from components.ShooterComponent import ShooterComponent

class Shoot(Command):
    
    def __init__(self):
        super.__init__()
        self.timer = Timer()

    def on_start(self):
        RobotMap.shooter_component.disable_intake()
        RobotMap.shooter_component.engage_launcher()
        self.timer.start()

    def execute(self):
        if self.timer.hasPeriodPassed(1.5):
            RobotMap.shooter_component.enable_intake()
            self.finished()
        elif self.timer.hasPeriodPassed(1.0):
            RobotMap.shooter_component.retract_launcher()
        
    def on_end(self):
        self.timer.stop()
        self.timer.reset()