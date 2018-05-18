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
from ctre import WPI_TalonSRX, FeedbackDevice, RemoteSensorSource, PigeonIMU, ParamEnum, ControlMode, NeutralMode
from wpilib.drive import DifferentialDrive
from Command import InstantCommand, Command
from wpilib.timer import Timer
from enum import Enum, auto
import math
from Events import Events
from pid_helpers import Gains, PIDOutput, PIDSource

class GearMode:
    OFF = auto()
    LOW = auto()
    HIGH = auto()


class DriverComponent(Events):

    def __init__(self):
        self.left_front = Talon()
        self.left_rear = Talon()
        self.right_front = Talon()
        self.right_rear = Talon()
        
        self.gear_solenoid = DoubleSolenoid()
        
        #self.driver_gyro = ADXRS450_Gyro()

        self._create_event(DriverComponent.EVENTS.driving)

    def set_curve(self, linear, angular):
        sf = abs(linear) + abs(angular)

        self.left_front.set((linear + angular)/sf)
        self.right_front.set((linear - angular)/sf)
        self.right_rear.set((linear - angular)/sf)
        self.left_rear.set((linear + angular)/sf)

    def toggle_gear(self):
        if self.current_gear() is GearMode.LOW:
            self.set_high_gear()
        if self.current_gear() is GearMode.HIGH:
            self.set_low_gear()

    def set_low_gear(self):
        print("shift low")
        self.gear_solenoid.set(DoubleSolenoid.Value.kReverse)

    def set_high_gear(self):
        print("shift high")
        self.gear_solenoid.set(DoubleSolenoid.Value.kForward)
