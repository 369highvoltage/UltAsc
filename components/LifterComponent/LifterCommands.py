from robot_map import RobotMap
from Command import InstantCommand, Command
from components.LifterComponent import LifterComponent


def move_lifter(speed: float) -> InstantCommand:
    def move_lifter_sync():
        RobotMap.lifter_component.set_elevator_speed(speed)
        RobotMap.lifter_component.set_carriage_speed(speed)
    return InstantCommand(move_lifter_sync)


class MoveToPosition(Command):
    def __init__(self, position: str):
        super().__init__()
        self._target_position = LifterComponent.positions[position]

    def on_start(self):
        print("start move to position command")

    def execute(self):
        RobotMap.lifter_component.lift_to_distance(self._target_position)
        if RobotMap.lifter_component.is_at_distance(self._target_position):
            self.finished()

    def on_end(self):
        print("endd move to position command")


def move_up_instant() -> InstantCommand:
    target_position = LifterComponent.positions[RobotMap.lifter_component.next_position()]
    return InstantCommand(lambda: RobotMap.lifter_component.lift_to_distance(target_position))


def move_down_instant() -> InstantCommand:
    target_position = LifterComponent.positions[RobotMap.lifter_component.prev_position()]
    return InstantCommand(lambda: RobotMap.lifter_component.lift_to_distance(target_position))


class Reset(Command):
    def on_start(self):
        pass

    def execute(self):
        speed = -0.25
        RobotMap.lifter_component.set_elevator_speed(speed)
        RobotMap.lifter_component.set_carriage_speed(speed)
        if RobotMap.lifter_component.elevator_bottom_switch.get() \
                and RobotMap.lifter_component.carriage_bottom_switch.get():
            RobotMap.lifter_component.reset_sensors()
            self.finished()

    def on_end(self):
        pass


class MoveUp(Command):
    def __init__(self):
        super().__init__()
        self._target_position = None

    def on_start(self):
        self._target_position = LifterComponent.positions[RobotMap.lifter_component.next_position()]

    def execute(self):
        RobotMap.lifter_component.lift_to_distance(self._target_position)
        if RobotMap.lifter_component.is_at_distance(self._target_position):
            self.finished()


class MoveDown(Command):
    def __init__(self):
        super().__init__()
        self._target_position = None

    def on_start(self):
        self._target_position = LifterComponent.positions[RobotMap.lifter_component.prev_position()]

    def execute(self):
        RobotMap.lifter_component.lift_to_distance(self._target_position)
        if RobotMap.lifter_component.is_at_distance(self._target_position):
            self.finished()
