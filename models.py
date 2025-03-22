from sqlalchemy import Column, Integer, Float, String, DateTime, Boolean, ForeignKey, func
from sqlalchemy.orm import relationship
from database import Base

class SensorData(Base):
    __tablename__ = "sensor_data"

    id = Column(Integer, primary_key=True, index=True)
    repetitions = Column(Integer, nullable=False)
    duration = Column(Float, nullable=False)
    difficulty = Column(Float, nullable=False)
    speed = Column(Float, nullable=False)
    amplitude = Column(Float, nullable=False)
    timestamp = Column(DateTime, default=func.now())

class AsymmetryData(Base):
    __tablename__ = "asymmetry_data"

    id = Column(Integer, primary_key=True, index=True)
    sensor_id = Column(Integer, nullable=False)  # Foreign key to sensor_data
    left_side_force = Column(Float, nullable=False)
    right_side_force = Column(Float, nullable=False)
    imbalance_percentage = Column(Float, nullable=False)
    timestamp = Column(DateTime, default=func.now())

class SensorStatus(Base):
    __tablename__ = "sensor_status"

    id = Column(Integer, primary_key=True, index=True)
    sensor_id = Column(Integer, nullable=False)  # Foreign key to sensor_data
    battery_level = Column(Float, nullable=False)
    firmware_version = Column(String, nullable=False)
    is_functional = Column(Boolean, default=True)
    last_update = Column(DateTime, default=func.now())
