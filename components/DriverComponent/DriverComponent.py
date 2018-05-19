from wpilib import \
    SpeedControllerGroup, \
    DoubleSolenoid, \
    ADXRS450_Gyro, \
    Joystick, \
    run, \
    DigitalInput, \
    AnalogPotentiometer, \
    Talon, \
    SmartDashboard, \
    Victor, \
    Compressor, \
    AnalogInput, \
    Ultrasonic, \
    PIDController
from ctre import WPI_TalonSRX, FeedbackDevice, PigeonIMU, ControlMode, NeutralMode
from wpilib.drive import DifferentialDrive
from Command import InstantCommand, Command
from wpilib.timer import Timer
from enum import Enum, auto
import math
from Events import Events
from pid_helpers import Gains, PIDOutput, PIDSource

class DriverComponent(Events):

    def __init__(self):
        self.left_front = Talon(2)
        self.left_rear = Talon(3)
        self.right_front = Talon(0)
        self.right_rear = Talon(1)
        
        self.gear_solenoid = DoubleSolenoid(6, 7)
        
        self.high_gear_enabled = False
        #self.driver_gyro = ADXRS450_Gyro()
        
        self.left_front.setInverted(True)
        self.left_rear.setInverted(True)
        self.set_low_gear()
        #self._create_event(DriverComponent.EVENTS.driving)
    
    def filter_deadband(self, value: float):
        if -0.1 < value < 0.1:
            return 0
        else:
            return value

    def set_curve_raw(self, linear, angular):
        pass

    def set_curve(self, linear, angular):
        l = self.filter_deadband(linear)
        a = self.filter_deadband(angular)
        sf = max(1, abs(l) + abs(a))

        self.left_front.set((l + a)/sf)
        self.right_front.set((l - a)/sf)
        self.right_rear.set((l - a)/sf)
        self.left_rear.set((l + a)/sf)

    def toggle_gear(self):
        self.high_gear_enabled = not self.high_gear_enabled
        if self.high_gear_enabled:
            self.set_high_gear()
        else:
            self.set_low_gear()

    def set_low_gear(self):
        print("shift low")
        self.gear_solenoid.set(DoubleSolenoid.Value.kReverse)

    def set_high_gear(self):
        print("shift high")
        self.gear_solenoid.set(DoubleSolenoid.Value.kForward)
