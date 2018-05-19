from wpilib import \
    Compressor, \
    DoubleSolenoid, \
    Relay, \
    SmartDashboard, \
    SpeedControllerGroup, \
    Talon

class ShooterComponent:
    
    def __init__(self):
        self.lower_shooter = Talon(4)
        self.upper_shooter = Talon(5)
        self.intake = Relay(1)

        self.launcher = DoubleSolenoid(4, 5)
        self.lifter = DoubleSolenoid(2, 3)

        self.should_lift = False
        self.is_shooting = False

        self.retract_launcher()
    
    def is_busy(self):
        return self.is_shooting
    
    def set_active(self):
        self.is_shooting = True
    
    def set_inactive(self):
        self.is_shooting = False

    def enable_intake(self):
        self.intake.set(Relay.Value.kReverse)
    
    def disable_intake(self):
        self.intake.set(Relay.Value.kOff)
    
    def engage_launcher(self):
        self.launcher.set(DoubleSolenoid.Value.kReverse)
    
    def retract_launcher(self):
        self.launcher.set(DoubleSolenoid.Value.kForward)

    def toggle_lifter(self):
        self.should_lift = not self.should_lift
        if self.should_lift:
            self.raise_lifter()
        else:
            self.lower_lifter()
    
    def raise_lifter(self):
        self.lifter.set(DoubleSolenoid.Value.kForward)
    
    def lower_lifter(self):
        self.lifter.set(DoubleSolenoid.Value.kReverse)
    
    def shoot(self, speed: float):
        self.lower_shooter.set(speed)
        self.upper_shooter.set(speed)