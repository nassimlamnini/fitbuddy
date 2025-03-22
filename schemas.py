from pydantic import BaseModel
from datetime import datetime


class SensorDataBase(BaseModel):
    repetitions: int
    duration: float
    difficulty: float
    speed: float
    amplitude: float

class SensorDataCreate(SensorDataBase):
    pass

class SensorDataResponse(SensorDataBase):
    id: int
    timestamp: datetime

    class Config:
        orm_mode = True

class AsymmetryDataBase(BaseModel):
    sensor_id: int  # Link to sensor_data
    left_side_force: float
    right_side_force: float
    imbalance_percentage: float

class AsymmetryDataCreate(AsymmetryDataBase):
    pass

class AsymmetryDataResponse(AsymmetryDataBase):
    id: int
    timestamp: datetime

    class Config:
        orm_mode = True

class SensorStatusBase(BaseModel):
    sensor_id: int  # Link to sensor_data
    battery_level: float
    firmware_version: str
    is_functional: bool = True

class SensorStatusCreate(SensorStatusBase):
    pass

class SensorStatusResponse(SensorStatusBase):
    id: int
    last_update: datetime

    class Config:
        orm_mode = True
