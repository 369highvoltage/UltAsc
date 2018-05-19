from robot_map import RobotMap
from Command import InstantCommand, Command
from wpilib.timer import Timer
from components.ShooterComponent import ShooterComponent

class Shoot(Command):
    
    def __init__(self):
        super().__init__()
        self.timer = Timer()
        self.phase = 0

    def on_start(self):
        self.phase = 0
        RobotMap.shooter_component.set_active()
        RobotMap.shooter_component.disable_intake()
        RobotMap.shooter_component.engage_launcher()
        self.timer.reset()
        self.timer.start()

    def execute(self):
        if self.phase == 0:
            if self.timer.hasPeriodPassed(0.5):
                print("first phase")
                RobotMap.shooter_component.retract_launcher()
                RobotMap.shooter_component.enable_intake()
                self.phase = 1
        elif self.phase == 1:
            if self.timer.hasPeriodPassed(1.0):
                print("second phase")
                RobotMap.shooter_component.disable_intake()
                self.finished()
                return
            
            
        
    def on_end(self):
        self.timer.stop()
        self.timer.reset()
        RobotMap.shooter_component.set_inactive()