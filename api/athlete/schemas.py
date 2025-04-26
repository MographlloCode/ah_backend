from pydantic import Field
from typing import Optional

from api.base.schemas import PersonBaseSchema

class AthleteSchema():
    class Base(PersonBaseSchema.Base):
        sport: str = Field(max_length=255)
        weight: float = Field(gt=0)
        height: int = Field(gt=0)
        
    class Update(Base):
        sport: Optional[str] = Field(max_length=255)
        weight: Optional[float] = Field(gt=0)
        height: Optional[int] = Field(gt=0)

class FootballAthleteSchema:
    class Base(AthleteSchema.Base):
        pref_leg: str = Field(max_length=255)
        jersey_number: int = Field(gt=0)
        position: str = Field(max_length=255)
        goals: int = Field(gt=0)
        assists: int = Field(gt=0)
        
    class Update(Base):
        pref_leg: Optional[str] = Field(max_length=255)
        jersey_number: Optional[int] = Field(gt=0)
        position: Optional[str] = Field(max_length=255)
        goals: Optional[int] = Field(gt=0)
        assists: Optional[int] = Field(gt=0)