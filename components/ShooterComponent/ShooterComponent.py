from wpilib import \
    Compressor, \
    DoubleSolenoid, \
    Relay, \
    SmartDashboard, \
    SpeedControllerGroup, \
    Talon

class ShooterComponent():
    def __init__(self):
        self.lower_shooter = Talon()
        self.upper_shooter = Talon()
        self.intake = Relay(0, Relay.Direction.kReverse)

        self.launcher = DoubleSolenoid(,)
        self.lifter = DoubleSolenoid(,)

        self.should_lift = False
    
    def enable_intake(self):
        self.intake.set(Relay.Value.kOn)
    
    def disable_intake(self):
        self.intake.set(Relay.Value.kOff)
    
    def engage_launcher(self):
        self.lifter.set(DoubleSolenoid.Value.kForward)
    
    def retract_launcher(self):
        self.lifter.set(DoubleSolenoid.Value.kReverse)

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