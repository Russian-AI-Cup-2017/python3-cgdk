from types import SimpleNamespace
from model.ActionType import ActionType
from model.VehicleType import VehicleType


class Move(SimpleNamespace):
    def __init__(self,
                 action: (None, ActionType) = None,
                 group: int = 0,
                 left: float = 0.0,
                 top: float = 0.0,
                 right: float = 0.0,
                 bottom: float = 0.0,
                 x: float = 0.0,
                 y: float = 0.0,
                 angle: float = 0.0,
                 factor: float = 0.0,
                 max_speed: float = 0.0,
                 max_angular_speed: float = 0.0,
                 vehicle_type: (None, VehicleType) = None,
                 facility_id: int = -1,
                 vehicle_id: int = -1):
        self.action = action
        self.group = group
        self.left = left
        self.top = top
        self.right = right
        self.bottom = bottom
        self.x = x
        self.y = y
        self.angle = angle
        self.factor = factor
        self.max_speed = max_speed
        self.max_angular_speed = max_angular_speed
        self.vehicle_type = vehicle_type
        self.facility_id = facility_id
        self.vehicle_id = vehicle_id
