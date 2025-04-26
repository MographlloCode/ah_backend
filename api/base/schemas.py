from pydantic import BaseModel, Field

from typing import Optional
from uuid import UUID, uuid4
from datetime import datetime, date

from core.utils import REQUIRED

class BaseSchema():
    class Base(BaseModel):
        id: UUID = Field(default_factory=uuid4)
        created_at: datetime = Field(default=datetime.now())
        updated_at: datetime = Field(default=datetime.now())
        created_by: UUID = Field()
        updated_by: Optional[UUID] = Field()
    
    class Update(Base):
        id: Optional[UUID] = Field()
        created_at: Optional[datetime] = Field()
        updated_at: Optional[datetime] = Field(default_factory=datetime.now)
        created_by: Optional[UUID] = Field()
        updated_by: Optional[UUID] = Field()
        
class PersonBaseSchema():
    class Base(BaseSchema.Base):
        first_name: str = Field(max_length=255)
        last_name: str = Field(max_length=255)
        birth_date: date = Field(default=date.today)
        nacionality: int = Field(default=0)
    
    class Update(BaseSchema.Update):
        first_name: Optional[str] = Field(max_length=255)
        last_name: Optional[str] = Field(max_length=255)
        birth_date: Optional[date] = Field()
        nacionality: Optional[int] = Field()